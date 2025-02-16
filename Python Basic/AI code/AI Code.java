EXAMPLE AI GENERATED JAVA CODE FOR THE DEMO
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;

public class MandelbrotSet extends JFrame {

    private final int WIDTH = 800;  // Width of the window
    private final int HEIGHT = 800; // Height of the window
    private final int MAX_ITER = 1000; // Maximum number of iterations
    private final double ZOOM = 400;  // Zoom level
    private BufferedImage image;  // The image buffer to draw on

    public MandelbrotSet() {
        super("Mandelbrot Set");
        setSize(WIDTH, HEIGHT);
        setResizable(false);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        image = new BufferedImage(WIDTH, HEIGHT, BufferedImage.TYPE_INT_RGB);
        createMandelbrot();
    }

    private void createMandelbrot() {
        for (int x = 0; x < WIDTH; x++) {
            for (int y = 0; y < HEIGHT; y++) {
                double zx = 0;
                double zy = 0;
                double cX = (x - WIDTH / 2.0) / ZOOM;
                double cY = (y - HEIGHT / 2.0) / ZOOM;
                int iter = MAX_ITER;
                while (zx * zx + zy * zy < 4 && iter > 0) {
                    double tmp = zx * zx - zy * zy + cX;
                    zy = 2.0 * zx * zy + cY;
                    zx = tmp;
                    iter--;
                }
                // Choose a color based on the number of iterations
                image.setRGB(x, y, iter | (iter << 8));
            }
        }
    }

    @Override
    public void paint(Graphics g) {
        g.drawImage(image, 0, 0, this);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            MandelbrotSet mandelbrot = new MandelbrotSet();
            mandelbrot.setVisible(true);
        });
    }
}