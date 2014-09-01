using System;

namespace Solution
{
	class JBit {
		byte[] _myArr;

		public JBit(int size) {
			_myArr = new byte[size >> 3]; //divide by eight
		}

		public bool Get(int pos) {
			int bytePos = pos >> 3;
			int bitPos = pos % 8;

			return (_myArr [bytePos] & (1 << bitPos)) != 0;
		}

		public void Set(int pos) {
			int bytePos = pos >> 3;
			int bitPos = pos % 8;
			_myArr [bytePos] |= (byte)(1 << bitPos);
		}
	}
}

