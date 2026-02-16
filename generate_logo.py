import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_logo():
    # Create figure
    fig, ax = plt.subplots(figsize=(5, 5), dpi=100)

    # Set background color (Dark Slate/Blue)
    bg_color = '#0f172a'
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    # Hide axes
    ax.set_xlim(0, 500)
    ax.set_ylim(0, 500)
    ax.axis('off')

    # Draw Bars (simulating the SVG design)
    # Matplotlib coordinates are bottom-left origin (0,0)
    # We map SVG (top-left origin) to Matplotlib

    # Bar 1: DII Sell (Red)
    # SVG: y=250, h=150 -> Bottom y=100, Top y=250
    ax.add_patch(patches.Rectangle((100, 100), 60, 150, color='#ef4444', alpha=1.0))

    # Bar 2: FII Buy (Green)
    # SVG: y=150, h=250 -> Bottom y=100, Top y=350
    ax.add_patch(patches.Rectangle((180, 100), 60, 250, color='#22c55e', alpha=1.0))

    # Bar 3: Sell (Red)
    # SVG: y=200, h=200 -> Bottom y=100, Top y=300
    ax.add_patch(patches.Rectangle((260, 100), 60, 200, color='#ef4444', alpha=1.0))

    # Bar 4: Buy (Green - High)
    # SVG: y=100, h=300 -> Bottom y=100, Top y=400
    ax.add_patch(patches.Rectangle((340, 100), 60, 300, color='#22c55e', alpha=1.0))

    # Add Glow effect (simulated with semi-transparent larger rects) is hard in simple mpl, skipping for clean vector look

    # Rupee Symbol Overlay
    # Centered at (250, 275) roughly
    ax.text(250, 275, '₹', fontsize=180, color='white', alpha=0.3,
            ha='center', va='center', fontweight='bold')

    # Text Label
    ax.text(250, 50, 'FII DII TRACKER', fontsize=20, color='#e2e8f0',
            ha='center', va='center', fontweight='bold')

    # Save
    plt.savefig('logo.png', facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight', pad_inches=0)
    print("Logo generated: logo.png")

if __name__ == "__main__":
    create_logo()
