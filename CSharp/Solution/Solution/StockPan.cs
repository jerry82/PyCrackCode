using System;
using System.Collections;
using System.Collections.Generic;

namespace Solution
{
	public class StockPan
	{
		int[] P = new int[] {100, 60, 70, 65, 80, 85};

		public StockPan ()
		{
		}

		public void Run() {
			List<int> panArr = new List<int> (); 
			Stack<int> S = new Stack<int> ();

			for (int i = 0; i < P.Length; i++) {
				int score = 1;
				while (S.Count > 0) {
					int itop = S.Peek ();
					int top = P [itop];

					if (P[i] > top) {
						int tmp = S.Pop ();
						score += panArr [tmp];
					} else 
						break;
				}

				panArr.Add (score);
				S.Push (i);
			}

			Print (panArr.ToArray());
		}

		public void Print(int[] arr) {
			foreach (int i in arr) {
				Console.Write (" {0} ", i);
			}
			Console.WriteLine ();
		}
	}
}

