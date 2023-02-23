public class WindInfo {
  
    public static String message(String rwy, int windDirection,int windSpeed) {
        int pilotAngel = Integer.parseInt(rwy.substring(0, 2));
        int i = pilotAngel * 10 - windDirection;
        double resultAngle =  Math.toRadians(i);
        int CW = (int) Math.abs(Math.round(Math.sin(resultAngle)*windSpeed));
        int HW = (int) Math.abs(Math.round(Math.cos(resultAngle)*windSpeed));
        String position1 = null;
        String position2 = null;
        position1 = Math.round(Math.cos(resultAngle)*windSpeed)<0  ? "Tail" : "Head";
      
        position2 = Math.round(Math.sin(resultAngle)*windSpeed)<=0 ? "right" : "left";

        return String.format("%swind %s knots. Crosswind %s knots from your %s.", position1,HW,CW,position2);
    }
  }
