from bisect import bisect_left
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()

        target = ""
        output = []
        for letter in searchWord:
            suggestions = []
            target += letter

            index = bisect_left(products, target)

            for i in range(index, min(index + 3,len(products))):
                if products[i].startswith(target):
                    suggestions.append(products[i])
                else:
                    print("APSOFKAPSF")
                    break

            output.append(suggestions)

        return output


