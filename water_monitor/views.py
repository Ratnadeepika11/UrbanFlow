from django.shortcuts import render, redirect
from .models import WaterSector
import matplotlib
matplotlib.use('Agg') # Required for web servers
import matplotlib.pyplot as plt
import pandas as pd
import io, base64

def dashboard(request):
    # 1. Handle Form Submission (If a user updates usage from the UI)
    if request.method == "POST":
        sector_id = request.POST.get('sector_id')
        new_usage = float(request.POST.get('usage', 0))
        sector = WaterSector.objects.get(id=sector_id)
        sector.consumption_liters = new_usage
        sector.save()
        return redirect('dashboard')

    # 2. Fetch Data & Prepare Pandas DataFrame
    sectors = WaterSector.objects.all()
    df = pd.DataFrame(list(sectors.values()))
    
    sector_data = []
    stats = {'total_inflow': 0, 'total_outflow': 0, 'nrw_loss': 0}
    graph = None

    if not df.empty:
        # --- NUMPY/PANDAS ANALYTICS ---
        total_in = df['inflow_liters'].sum()
        total_out = df['consumption_liters'].sum()
        nrw = total_in - total_out
        
        stats = {
            'total_inflow': total_in,
            'total_outflow': total_out,
            'nrw_loss': round(nrw, 2),
            'loss_percent': round((nrw / total_in * 100), 1) if total_in > 0 else 0
        }

        # --- SECTOR-WISE LOGIC ---
        for s in sectors:
            usage = float(s.consumption_liters)
            limit = float(s.threshold)
            loss = s.inflow_liters - usage
            
            # Alert Logic
            is_leak = loss > (s.inflow_liters * 0.15) 
            is_over_limit = usage > limit             
            
            sector_data.append({
                'id': s.id,
                'name': s.sector_name, # Ensure this matches your model field
                'usage': usage,
                'limit': limit,
                'loss': round(loss, 2),
                'ph': s.ph_level,
                'pressure': s.pressure_bar,
                'leak_alert': is_leak,
                'threshold_alert': is_over_limit,
                'quality_alert': not (6.5 <= s.ph_level <= 8.5),
                'pressure_alert': s.pressure_bar < 2.0 or s.pressure_bar > 6.0,
            })

        # --- MATPLOTLIB VISUALIZATION ---
        plt.figure(figsize=(8, 4))
        colors = []
        for item in sector_data:
            if item['threshold_alert']: colors.append('#e74c3c') # Red
            elif item['leak_alert']: colors.append('#f39c12')   # Orange
            else: colors.append('#3498db')                      # Blue
            
        # Note: Ensure 'name' or 'sector_name' matches your model
        plt.bar([s.sector_name for s in sectors], [s.consumption_liters for s in sectors], color=colors)
        plt.title('Urban Analysis: Blue (Ok), Red (Waste), Orange (Leak)')
        plt.xlabel('City Sectors')
        plt.ylabel('Consumption (Liters)')
        
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight')
        graph = base64.b64encode(buffer.getvalue()).decode()
        plt.close()

    # 3. Render the Template
    return render(request, 'dashboard.html', {
        'sector_data': sector_data, 
        'graph': graph, 
        'stats': stats, 
        'sectors': sectors
    })