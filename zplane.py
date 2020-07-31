import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

def z_plane3D(b, a = [], extent = [-2, 2, -2, 2], figsize_ = [10, 7]):

    """
    Plots the poles and zeros as 3D plot showing the placement in the complex plane with the mangitude response.
    Also plots the phase response on the complex plane.

    Made by Martin Soria Røvang
    """
    if len(a) < 1:
        a = np.zeros(len(b))
        a[0] = 1
    b_ = np.poly1d(b)
    a_ = np.poly1d(a)
    roots_b = b_.r
    roots_a = a_.r
    b_ = np.flip(b_)
    a_ = np.flip(a_)


    x_lin = np.linspace(extent[0], extent[1], 2000)
    y_lin = np.linspace(extent[2], extent[3], 2000)
    x_mesh, y_mesh = np.meshgrid(x_lin, y_lin)

    z = x_mesh + 1j*y_mesh

    H_b = np.polyval(b_, 1/z)
    H_a = np.polyval(a_, 1/z)
    H = np.divide(H_b, H_a)
    
    H_magnitude = np.abs(H)
    phase = np.angle(H)
    circle = np.linspace(0,2*np.pi, 2000)

    fig, ax = plt.subplots(1, 2, figsize = figsize_)
    img1 = ax[1].imshow(phase, cmap = 'jet', extent = extent)
    ax[1].plot(np.cos(circle), np.sin(circle), '--', color = 'white')
    img2 = ax[0].imshow(H_magnitude, vmin = 0, vmax = 1, cmap = 'jet', extent = extent)
    ax[0].plot(np.cos(circle), np.sin(circle), '--', color = 'white')
    ax[0].plot(np.real(roots_b), np.imag(roots_b), 'o', color = 'yellow',label = 'Zeros', markersize = 5)
    ax[0].plot(np.real(roots_a), np.imag(roots_a), 'X', color = 'black',label = 'Poles', markersize = 5)
    ax[0].set_title('$|\mathcal{H}(z)|$', fontsize = '15')
    ax[0].set_xlabel('Real axis')
    ax[0].set_ylabel('Imaginary axis')
    ax[1].set_title('$\\angle\\mathcal{H}(z)$ (Phase response)', fontsize = '15')
    ax[1].set_xlabel('Real axis')
    ax[1].set_ylabel('Imaginary axis')
    ax[0].legend()
    divider = make_axes_locatable(ax[1])
    cax = divider.append_axes('right', size='5%', pad=0.05)
    fig.colorbar(img1, cax=cax, orientation='vertical')
    divider = make_axes_locatable(ax[0])
    cax = divider.append_axes('right', size='5%', pad=0.05)
    fig.colorbar(img2, cax=cax, orientation='vertical')
    plt.tight_layout()
    plt.show()
    
    return H, b_, a_



b = np.ones(4)/4

z_plane3D(b)