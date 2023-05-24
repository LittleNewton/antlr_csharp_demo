using Antlr4.Runtime;
using System;
using System.Numerics;  

namespace antlr_csharp
{
    class MyCalculator
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter an arithmetic expression:");
            string input = Console.ReadLine();

            // Create a lexer and parser for the input expression
            var inputStream = new AntlrInputStream(input);
            var lexer = new CalculatorLexer(inputStream);
            var commonTokenStream = new CommonTokenStream(lexer);
            var parser = new CalculatorParser(commonTokenStream);

            // Parse the input expression and retrieve the parse tree
            var parseTree = parser.calc();

            // Create a visitor instance and visit the parse tree
            var visitor = new MyVisitor();
            var result = visitor.Visit(parseTree);

            Console.WriteLine($"Result: {result}");
        }
    }
}
