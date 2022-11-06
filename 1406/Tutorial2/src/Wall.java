public class Wall extends StationaryObject{
    private int		    width;
    private int		    height;

    public Wall(Point2D loc, int w, int h) {
        super(loc);
        width = w;
        height = h;
    }

    // The get/set methods

    public int getWidth() { return width; }
    public int getHeight() { return height; }


    public String toString() {
        return "Wall" + " at (" + (int)location.getX() + "," + (int)location.getY() + ") with width " +
                width + " and height " + height;
    }
}