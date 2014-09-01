using System;

namespace Solution
{
	public class SubsequenceSum
	{
		public SubsequenceSum ()
		{
		}

		public void Run() {
			int[] A = new int[] { -2, -3, 4, -1, -2, 1, 5, -3, -100, 100 };

			int l = A.Length;
			int[] S = new int[l];
			int[][] I = new int[l][]; 

			//Si = max { Si-1 + Ai, Ai }
			S [0] = A [0];
			I [0] = new int[] { 0, 0 };

			int prevI = I[0][1];

			for (int i = 1; i < l; i++) {

				I [i] = new int[] { -1, -1 };

				int max = A [i];

				if (max < A [i] + S [i - 1]) {
					max = A [i] + S [i - 1];
					if (prevI == -1) {
						prevI = i - 1;
					}
					I [i] = new int[] { prevI, i };
				}
				else {
					I [i] [1] = i;
					prevI = -1;
					I [0][0] = prevI;
				}

				S [i] = max;
			}

			Print (A);
			Print (S);
			PrintSeq (I);

			Console.ReadLine ();
		}

		void Print(int[] arr) {
			foreach (int n in arr) {
				Console.Write (" {0}\t", n);
			}
			Console.WriteLine ();
		}

		void PrintSeq(int[][] arr) {
			foreach (int[] i in arr) {
				Console.Write (" {0}|{1}\t", i [0], i [1]);
			}
			Console.WriteLine ();
		}

	}
}

