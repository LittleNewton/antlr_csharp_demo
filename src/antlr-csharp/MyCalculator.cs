using Antlr4.Runtime;
using System;
using System.Numerics;  

namespace antlr_csharp
{
    class MyCalculator
    {
        static void Main(string[] args)
        {
            // Prompt words
            Console.WriteLine("Calculator Program");
            Console.WriteLine("Enter 'q' to quit.");

            int result;

            while (true)
            {
                string input = Console.ReadLine();
                if (input == "q")
                {
                    break;
                }
                else
                {
                    try
                    {
                        result = evaluate(input);
                        Console.WriteLine(result);
                    }
                    catch
                    {
                        throw new Exception("Wow.");
                    }
                }
            }
        }

        /// <summary>
        /// 调用解析器 visitor 模式，求得返回值。
        /// </summary>
        /// <param name="expr"></param>
        /// <returns></returns>
        static int evaluate(string expr)
        {
            int result;

            // Create a lexer and parser for the input expression
            var inputStream = new AntlrInputStream(expr);
            var lexer = new CalculatorLexer(inputStream);
            var commonTokenStream = new CommonTokenStream(lexer);
            var parser = new CalculatorParser(commonTokenStream);

            // Parse the input expression and retrieve the parse tree
            var parseTree = parser.calc();
            
            // Create a visitor instance and visit the parse tree
            var visitor = new MyVisitor();
            result = visitor.Visit(parseTree);

            return result;
        }
    }
}
