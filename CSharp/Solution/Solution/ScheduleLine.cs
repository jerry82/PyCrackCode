using System;

namespace Solution
{
	public class ScheduleLine
	{
		int[,] A = new int[2, 4] { {4, 5, 3, 2}, {2, 10, 1, 4} };
		int[] T12 = new int[] {0, 7, 4, 5};
		int[] T21 = new int[] {0, 9, 2, 8};
		int[] E = new int[] {10, 12};
		int[] X = new int[] {18, 7};

		//[sum1, node]
		int[,] L1 = new int [4, 2] { {0, -1}, {0, -1}, {0, -1}, {0, -1}};
		int[,] L2 = new int [4, 2] { {0, -1}, {0, -1}, {0, -1}, {0, -1}};

		public ScheduleLine ()
		{
			PrintL ();
		}

		public void Run() {
			for (int i = 1; i <= 4; i++) {
				int idx = i - 1;
				if (idx == 0) {
					L1 [idx, 0] = E [0] + A [0, 0];
					L1 [idx, 1] = -1;
					L2 [idx, 0] = E [1] + A [1, 0];
					L2 [idx, 1] = -1;
					continue;
				}

				//line1
				int tmp1 = L1 [idx - 1, 0] + A [0, idx];
				int tmp2 = L2 [idx - 1, 0] + A [0, idx] + T21 [idx];

				if (tmp1 <= tmp2) {
					L1 [idx, 0] = tmp1;
					L1 [idx, 1] = 1;
				} else {
					L1 [idx, 0] = tmp2;
					L1 [idx, 2] = 2;
				}


				//line2
				tmp1 = L1 [idx - 1, 0] + A [1, idx] + T12 [idx];
				tmp2 = L2 [idx - 1, 0] + A [1, idx];

				if (tmp1 <= tmp2) {
					L2 [idx, 0] = tmp1;
					L2 [idx, 1] = 1;
				} else {
					L2 [idx, 0] = tmp2;
					L2 [idx, 1] = 2;
				}


				if (i == 4) {
					L1 [idx, 0] += X [0];
					L2 [idx, 0] += X [1];
				}
			}

			PrintL ();

			//backtracking
		}

		public void PrintL() {
			Console.WriteLine();
			for (int i = 0; i < 4; i++) {
				Console.Write(" ({0},{1}) ", L1[i, 0], L1[i, 1]);
			}
			Console.WriteLine ();
			for (int i = 0; i < 4; i++) {
				Console.Write(" ({0},{1}) ", L2[i, 0], L2[i, 1]);
			}
			Console.WriteLine ();
		}
	}
}

