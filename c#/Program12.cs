using System;

namespace CaesarCipher
{
  class Program
  {
    static void Main(string[] args)
    {
      char[] alphabet = new char[] {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
      Console.WriteLine("Enter your secret message!");
      string message = Console.ReadLine();
      char[] secretMessage = message.ToCharArray();
      char[] encryptedMessage = new char[secretMessage.Length];
      for(int i=0; i<secretMessage.Length; i++) {
        char letter = secretMessage[i];
        int position = Array.IndexOf(alphabet, letter);
        int newPosition = (position + 3) % 26;
        char newLetter = alphabet[newPosition];
        encryptedMessage[i] = newLetter;
      }
      string newMessage = String.Join("", encryptedMessage);
      Console.WriteLine(newMessage);
    }
  }
}