using System;
using System.Collections;
using System.Collections.Generic;

namespace Solution
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			byte[] bytes = new byte[2];

			BitArray bits = new BitArray (bytes);

			foreach (Object obj in bits) {
				Console.Write ("{0} ", obj);
			}

			Console.ReadLine ();


		}
	}
}
