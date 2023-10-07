using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Numerics;

namespace antlr_csharp
{
    class MyVisitor : CalculatorBaseVisitor<int>
    {
        public override int VisitNumber(CalculatorParser.NumberContext context)
        {
            return int.Parse(context.NUM().GetText());
        }

        public override int VisitPlusOrMinusExpr(CalculatorParser.PlusOrMinusExprContext context)
        {
            int value = Visit(context.expr());
            if (context.PLUS() != null)
            {
                return value;
            }
            else if (context.MINUS() != null)
            {
                return -1 * value;
            }
            else
            {
                Console.WriteLine("非法操作符");
                return -1;
            }
        }

        public override int VisitInfixExpr(CalculatorParser.InfixExprContext context)
        {
            int left = Visit(context.left);
            int right = Visit(context.right);
            string op = context.op.Text;

            if (op == "*")
            {
                return left * right;
            }
            else if (op == "/")
            {
                if (right != 0)
                {
                    return left / right;
                }
                else
                {
                    Console.WriteLine($"除数不能为零");
                    return -1;
                }
            }
            else if (op == "+")
            {
                return left + right;
            }
            else if (op == "-")
            {
                return left - right;
            }
            else
            {
                throw new InvalidProgramException("What?");
            }
        }

        public override int VisitParensExpr(CalculatorParser.ParensExprContext context)
        {
            return Visit(context.expr());
        }
    }
}
