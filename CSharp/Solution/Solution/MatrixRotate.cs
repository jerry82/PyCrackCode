using System;
using System.Collections;
using System.Collections.Generic;

namespace Solution
{
	public class MatrixRotate
	{
		List<List<String>> B = new List<List<String>>();

		public MatrixRotate ()
		{
			B.Add (new List<String> (new String[] { "*", "*", "*", "0", "*", "*", "*" } ));
			B.Add (new List<String> (new String[] { "*", "*", "*", "&", "*", "*", "*" } ));
			B.Add (new List<String> (new String[] { "*", "*", "*", "&", "*", "*", "*" } ));
			B.Add (new List<String> (new String[] { "*", "*", "*", "&", "*", "*", "*" } ));
		}

		public void Run() {

			//extend array
			int row = B.Count;
			int col = B [0].Count;
			List<List<String>> C = new List<List<string>> ();
			int tmp1 = col; 
			int tmp2 = row;
			//resize vertical
			if (col < row) {
				tmp1 = row;
				tmp2 = col;
			}
				
			//build C 
			for (int i = 0; i < tmp1; i++) {
				C.Add (PadLine (tmp2));
			}

			//swap
			for (int r = 0; r < row; r++) {
				for (int c = 0; c < col; c++) {
					C [c] [row - r - 1] = B [r] [c];
				}
			}

			Print(C);
		}

		private List<String> PadLine(int size) {
			String[] arr = new String[size];
			for (int i = 0; i < size; i++) {
				arr [i] = "-";
			}
			return new List<String> (arr);
		}

		public void Print(List<List<String>> tmp) {
			foreach (List<String> l in tmp) {
				foreach (String s in l) {
					Console.Write (" {0} ", s);
				}
				Console.WriteLine ();
			}
		}
	}
}

