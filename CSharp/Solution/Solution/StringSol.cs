using System;

namespace Solution
{
	public class StringSol
	{
		public StringSol ()
		{
		}

		/* sort string then check next */
		public void Run(String tmp) {

			Char[] chars = tmp.ToCharArray ();
			SortString (chars, 0, tmp.Length - 1);

			Console.WriteLine (new String(chars));

			/*
			if (chars.Length <= 1) {
				Console.WriteLine ("unique");
				return;
			}

			char prevC = chars[0];
			for (int i = 1; i < chars.Length; i++) {
				if (chars [i] != prevC) {
					prevC = chars [i];
				} else {
					Console.WriteLine ("not unique");
					return;
				}
			}

			Console.WriteLine ("unique");
			*/
		}

		//quick sort
		public void SortString(Char[] input, int start, int end) {
		
			if (end <= start)
				return;

			Random r = new Random ();
			int randomIdx = r.Next (start, end);
			Char piv = input [randomIdx];

			piv = input [start];

			int i = start + 1;
			int j = end;

			while (i < j) {

				while (input [i] < piv) {
					i++;
					if (i > end)
						break;
				}

			
				while (input [j] > piv) {
					j--;
					if (j < start)
						break;
				}

				if (j > i) {
					Char tmp = input [i];
					input [i] = input [j];
					input [j] = tmp;
					i++;
					j--;
				}
			}
				
			Char tmp2 = input[start];
			input [start] = input [i - 1];
			input [i - 1] = tmp2;

			SortString (input, start, i - 1);
			SortString (input, i, end);
		}
	}
}
