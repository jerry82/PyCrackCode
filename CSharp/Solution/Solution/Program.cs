using System;
using System.Threading;
using System.Collections;
using System.Collections.Generic;

namespace Solution
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			Console.WriteLine ("shuffle 10 numbers");
			int[] arr = new int[10];

			for (int i = 0; i < 10; i++) {
				arr [i] = i * 10;
			}
			Print (arr);

			Console.WriteLine ("after shuffle");
			Random r = new Random ();

			for (int i = 0; i < 10; i++) {

				int t = r.Next (i, 9);
				//swap with first element
				int tmp = arr [i];
				arr [i] = arr [t];
				arr [t] = tmp;
			}


			Print (arr);

			Console.WriteLine ();
		}

		static void Print(int[] arr) {
			foreach (int i in arr) {
				Console.Write (" {0} ", i);
			}
			Console.WriteLine ();
		}
	}
}
