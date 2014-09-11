using System;

namespace Solution
{
	public class Palindrome
	{
		//string str = @"dsfaaddffbobkayakbobaabbca";
		string str = @"aaaabobkayakbobaaggaaaaaaaaaaaaaaaaaaaabb";
		public Palindrome ()
		{
		}

		public void Run() {
			int maxlength = 0;
			int maxIdx = 0;
			int prev = 0;

			int length = 1;

			bool keepLeftP = false;
			bool firstTimePrev = true;
			bool same = false;

			bool foundOddPal = false;

			for (int i = 1; i < str.Length; i++) {

				if (!foundOddPal && str [i] == str [i - 1]) {
					if (firstTimePrev) {
						prev = i - 1;
						firstTimePrev = false;
					}
					length++;
					same = true;
					Console.WriteLine ("found even pal with length = {0} at {1}", length, prev);
					continue;
				}

				//if prev same
				if (same) {
					same = false;
					firstTimePrev = true;
					if (length > maxlength) {
						maxlength = length;
						maxIdx = prev;
						length = 1;
					}
				}

				//check odd palindrome
				if (!foundOddPal)
					prev = i - 1;

				if (prev - 1 >= 0) {
					if (str [prev - 1] == str [i]) {
						length += 2;
						foundOddPal = true;
						prev--;
						Console.WriteLine ("found odd pal with length = {0}", length);
						continue;
					} else {
						foundOddPal = false;

						if (length > maxlength) {
							maxlength = length;
							maxIdx = prev - 1;
						}

						length = 1;
					}
				}

				Console.WriteLine (str);
				Console.Write ("at character: {0} -> {1}, maxlength: {2}, maxIdx: {3}", i, str[i], maxlength, maxIdx);
				//Console.ReadLine ();
				Console.WriteLine ();
			}

			if (length > maxlength) {
				maxlength = length;
				maxIdx = prev;
			}


			Console.Write ("conclusion -> maxlength: {0}, maxIdx: {1}", maxlength, maxIdx);
		}
	}
}

