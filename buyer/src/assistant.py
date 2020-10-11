class Assistant:

    def findProducts(self, category, userIdMap):
        recommendedProducts = {'primary': [], 'secondary': []}
        for product in category.get('products'):
            filterBitmap = [0] * len(userIdMap)
            for assisterId in range(len(userIdMap)):
                # The default value was selected
                if 0 in userIdMap[assisterId]:
                    filterBitmap[assisterId] = 1
                    continue

                # Compare product's filters with the user's filters
                for filterId in product.get('idMap')[assisterId]:
                    if filterId in userIdMap[assisterId]:
                        filterBitmap[assisterId] = 1
                        break

            # Store any primary or secondary matches
            if filterBitmap.count(1) == len(userIdMap):
                recommendedProducts.get('primary').append(product)
            elif filterBitmap.count(1) == len(userIdMap) - 1:
                recommendedProducts.get('secondary').append(product)

        # Provide recommended products
        report = ''
        for section in recommendedProducts:
            productNames = [product.get('name') for product in recommendedProducts.get(section)]
            if productNames:
                report += '{}: {}'.format(section.capitalize(), ', '.join(productNames))
            report += '\n'

        return report
