public class Trap extends StationaryObject implements Harmful{

    public Trap(Point2D loc) {
        super(loc);
    }

    @Override
    public int getDamageAmount() {
        return -50;
    }

    public String toString() {
        return "Trap" + " at (" + (int)location.getX() + "," + (int)location.getY() + ")";
    }
}