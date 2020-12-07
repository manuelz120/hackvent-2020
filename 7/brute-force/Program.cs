using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace brute_force
{
    class Program
    {
        static void FlagDecoder(char first, char second)
        {
            try
            {
                char[] charArray1 = "_B_u_m_B_u_m_W_i_t_h_T_h_e_T_u_m_T_u_m".ToCharArray();
                charArray1[8] = first;
                charArray1[14] = second;
                string str1 = "";
                for (int index = 0; index < charArray1.Length; ++index)
                {
                    if (index % 2 == 0 && index + 2 <= charArray1.Length)
                        str1 += charArray1[index + 1].ToString();
                }
                string str2;
                if (str1 == "BumBumWithTheTumTum")
                {
                    str2 = "SFYyMH" + charArray1[17].ToString() + "yMz" + (object)(charArray1[8].GetHashCode() % 10) + "zcnMzXzN" + charArray1[3].ToString() + "ZzF" + charArray1[9].ToString() + "MzNyM" + charArray1[13].ToString() + "5n" + charArray1[14].ToString() + "2";
                }
                else
                {
                    if (str1 == "")
                    {
                        Console.WriteLine("Your input is not allowed to result in an empty string");
                        return;
                    }
                    str2 = str1;
                }
                char[] charArray2 = "htroFdnAkcaB".ToCharArray();
                string str3 = "";
                Array.Reverse((Array)charArray2);
                for (int index = 0; index < charArray2.Length; ++index)
                    str3 += charArray2[index].ToString();
                string s;
                if (str3 == "BackAndForth")
                {
                    s = "Q1RGX3" + charArray2[11].ToString() + "sNH" + charArray2[8].ToString() + "xbm" + charArray2[5].ToString() + "f";
                }
                else
                {
                    if (str3 == "")
                    {
                        Console.WriteLine("Your input is not allowed to result in an empty string");
                        return;
                    }
                    s = str3;
                }
                char[] charArray3 = "nOMNSaSFjC[".ToCharArray();
                string str4 = "";
                byte num = 42;
                for (int index = 0; index < charArray3.Length; ++index)
                {
                    char ch = (char)((uint)charArray3[index] ^ (uint)num);
                    num = (byte)((int)num + index - 4);
                    str4 += ch.ToString();
                }
                string str5;
                if (str4 == "DinosAreLit")
                {
                    str5 = "00ZD" + charArray3[3].ToString() + "f" + charArray3[2].ToString() + "zRzeX0=";
                }
                else
                {
                    if (str4 == "")
                    {
                        Console.WriteLine("Your input is not allowed to result in an empty string");
                        return;
                    }
                    str5 = str4;
                }
                byte[] bytes = Convert.FromBase64String(str2 + str5);
                byte[] numArray1 = Convert.FromBase64String(s);
                byte[] buffer = new byte[bytes.Length];
                for (int index = 0; index < bytes.Length; ++index)
                    buffer[index] = (byte)((uint)bytes[index] ^ (uint)numArray1[index % numArray1.Length]);
                byte[] hash = SHA1.Create().ComputeHash(buffer);
                byte[] numArray2 = new byte[20]
                {
          (byte) 107,
          (byte) 64,
          (byte) 119,
          (byte) 202,
          (byte) 154,
          (byte) 218,
          (byte) 200,
          (byte) 113,
          (byte) 63,
          (byte) 1,
          (byte) 66,
          (byte) 148,
          (byte) 207,
          (byte) 23,
          (byte) 254,
          (byte) 198,
          (byte) 197,
          (byte) 79,
          (byte) 21,
          (byte) 10
                };
                for (int index = 0; index < hash.Length; ++index)
                {
                    if ((int)hash[index] != (int)numArray2[index])
                    {
                        Console.WriteLine("Your inputs do not result in the flag.");
                        return;
                    }
                }
                string str6 = Encoding.ASCII.GetString(bytes);
                if (!str6.StartsWith("HV20{"))
                    return;
                Console.WriteLine("Congratulations! You're now worthy to claim your flag: {0}", (object)str6);
            }
            catch
            {
            }
            finally
            {
            }

        }

        static void Main(string[] args)
        {
            var charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".ToCharArray();
            foreach (var char1 in charset)
            {
                foreach (var char2 in charset)
                {
                    FlagDecoder(char1, char2);
                }
            }
            Console.WriteLine("DONE");
            Console.ReadLine();
        }
    }
}
