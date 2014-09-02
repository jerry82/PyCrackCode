using System;
using System.Collections;
using System.Collections.Generic;

namespace Solution
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			StringSol s = new StringSol ();
			s.AllUniqueChar ("kdjfa;dsfjka;dsfjdsa;jfa");

			/*
			String st = "abcdeffgac";
			Char[] chars = st.ToCharArray();
			chars[0] = chars[1];

			Console.WriteLine(new String(chars));
			*/
			Console.ReadLine ();
		}
	}
}
