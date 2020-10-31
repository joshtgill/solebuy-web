class Assistant:

    def filterProducts(self, products, AFIdMap):
        filteredProducts = {'primary': [], 'secondary': []}
        for product in products:
            filterBitmap = [0] * len(AFIdMap)
            for assisterId in range(len(AFIdMap)):
                # If no filters exists for asssister, then pass it
                if not AFIdMap[assisterId]:
                    filterBitmap[assisterId] = 1
                    continue

                # Compare product's filters with the user's filters
                for assisterFilterId in product.assisterFilterIds.all():
                    if (assisterFilterId.assisterId == assisterId and
                        assisterFilterId.filterId in AFIdMap[assisterId]):
                        filterBitmap[assisterId] = 1
                        break

            # Store any primary or secondary matches
            if filterBitmap.count(1) == len(AFIdMap):
                filteredProducts.get('primary').append(product)
            elif filterBitmap.count(1) == len(AFIdMap) - 1:
                filteredProducts.get('secondary').append(product)

        return filteredProducts
