public class CubeFRUBDling {

    private static int[][][] cube =  // face ,y, x  ------------------------/       i( character, orientation )
                                        {{{i('6',3),i('_',1),i('e',3)},   //           0 -   0Â°
                                         {i('i',3),i('{',0),i('a',0)},   //           1 -  90Â°
                                        {i('e',1),i('s',1),i('3',1)}},  //           2 - 180Â°
      {{i('H',0),i('V',0),i('7',0)},                                   //           3 - 270Â°
      {i('h',0),i('_',1),i('e',1)},                                   //
     {i('o',0),i('a',2),i('_',2)}}, {{i('_',1),i('w',1),i(' ',0)},   //            <-- here the JElf lost his spot ;)
                                    {i(' ',0),i(' ',0),i(' ',0)},   //
                                   {i(' ',0),i(' ',0),i(' ',0)}}, {{i(' ',0),i(' ',0),i(' ',0)},
                                                                  {i(' ',0),i(' ',0),i(' ',0)},
                                                                 {i(' ',0),i(' ',0),i(' ',0)}}, {{i(' ',0),i(' ',0),i(' ',0)},
                                                                                                {i(' ',0),i(' ',0),i(' ',0)},
                                                                                               {i(' ',0),i(' ',0),i(' ',0)}},
                             {{i(' ',0),i(' ',0),i(' ',0)},  //
                             {i(' ',0),i(' ',0),i(' ',0)},  //
                            {i(' ',0),i(' ',0),i(' ',0)}}};//

    private static String[] rotations = {"F","R","U","B","L","D"};

    public static void main(String[] args) {

        // toDo: implement brute force algorithm

        System.out.println(readOut());
    }

    private static String readOut() {
        StringBuilder sb = new StringBuilder();
        for (int[][] side : cube) {
            for (int y = 0; y < 3; y++)
                for (int x = 0; x < 3; x++)
                    sb.append((char)(side[y][x]&0xff));
        }
        return sb.toString();
    }

    private static boolean check() {
        for (int[][] side : cube) {
            int rot = side[0][0] >> 8;
            for (int[] line : side)
                for (int c : line)
                    if (c >> 8 != rot)
                        return false;
        }
        return true;
    }
    private static void rotate(String direction) { // should perform all 18 variants F  R  U  B  L  D
        int help = 0;                              //                                F2 R2 U2 B2 L2 D2
        if (direction.endsWith("'")) {             //                                F' R' U' B' L' D'
            direction = direction.substring(0,1);
            rotate(direction);
            rotate(direction);
        }
        else if (direction.endsWith("2")) {
            direction = direction.substring(0,1);
            rotate(direction);
        }
        else if (direction.endsWith(" "))
            direction = direction.substring(0,1);

        switch (direction) {
            case "F" : // turn front clock wise
                help = cube[0][2][0];
                cube[0][2][0] = flipRight(cube[1][2][2]);
                cube[1][2][2] = flipRight(cube[5][0][2]);
                cube[5][0][2] = flipRight(cube[3][0][0]);
                cube[3][0][0] = flipRight(help);
                help = cube[0][2][1];
                cube[0][2][1] = flipRight(cube[1][1][2]);
                cube[1][1][2] = flipRight(cube[5][0][1]);
                cube[5][0][1] = flipRight(cube[3][1][0]);
                cube[3][1][0] = flipRight(help);
                help = cube[0][2][2];
                cube[0][2][2] = flipRight(cube[1][0][2]);
                cube[1][0][2] = flipRight(cube[5][0][0]);
                cube[5][0][0] = flipRight(cube[3][2][0]);
                cube[3][2][0] = flipRight(help);
                help = cube[2][0][0];
                cube[2][0][0] = flipRight(cube[2][2][0]);
                cube[2][2][0] = flipRight(cube[2][2][2]);
                cube[2][2][2] = flipRight(cube[2][0][2]);
                cube[2][0][2] = flipRight(help);
                help = cube[2][1][0];
                cube[2][1][0] = flipRight(cube[2][2][1]);
                cube[2][2][1] = flipRight(cube[2][1][2]);
                cube[2][1][2] = flipRight(cube[2][0][1]);
                cube[2][0][1] = flipRight(help);
                cube[2][1][1] = flipRight(cube[2][1][1]);
                break;
            case "R" :
                // toDo: turn right side up

                break;
            case "U" :
                // toDo: turn upper side clock wise

                break;
            case "B" :
                // toDo: turn back level right

                break;
            case "L" :
                // toDo: turn left side clock wise

                break;
            case "D" :
                // toDo: turn lower row right

                break;
        }
    }

    private static int flipRight(int content) {
        return (content+256) & 1023;        // using bit 9 and 10 for coding the orientation of the character
    }

    private static int i(char c, int orientation) {
        return c | (orientation << 8);      // glue the character and the orientation together
    }
}