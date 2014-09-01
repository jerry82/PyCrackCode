using System;

namespace Solution
{
	public class PermuteString
	{
		private String myString = String.Empty;

		public PermuteString (String a)
		{
			this.myString = a;
		}

		public void Run() {
			Permute("", myString);
			Console.WriteLine ();
		}

		public void Permute(string carry, string leftOver) {
		
			if (leftOver.Length == 1) {
				Console.WriteLine (carry + leftOver);
				return;
			}

			for (int i = 0; i < leftOver.Length; i++) {
				String tmpCarry = carry;

				carry += leftOver [i];
				String tmp = leftOver;
				tmp = tmp.Remove (i, 1);
				Permute (carry, tmp);

				carry = tmpCarry;
			}
		}
	}
}

