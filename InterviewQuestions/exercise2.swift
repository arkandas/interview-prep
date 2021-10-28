func searchQuotesForToy(toy: String, quotes: [String]) -> Int {
    var result = 0
    quotes.map({ String($0.lowercased())}).forEach({ quote in
        if quote.contains(toy.lowercased()) {
            result += 1
        }
    })
    return result
}

func popularNToys(numToys: Int, topToys: Int, toys:[String], numQuotes: Int, quotes: [String]) -> [String] {
    var array: [(toy: String, quotesForToy: Int)] = toys.map({ element in
        return (toy: element, quotesForToy: searchQuotesForToy(toy: element, quotes: quotes))
    })

    array.sort() {  if $0.quotesForToy != $1.quotesForToy {
        return $0.quotesForToy > $1.quotesForToy
    } else {
        return $0.toy.lowercased() < $1.toy.lowercased()
        }
    }
    print(array)
    return Array(array.map({$0.toy}).prefix(topToys))
}

func test() {
    let toys = ["elmo","elsa","legos","drone","tablet","warcraft"]
    let quotes = ["Elmo is the hottest toy elsa , Elmo elmo elMo el mo is perfect","The new elmo dolls","Expect elsa bla","Elsa and Elmo will be the","look into buying a drone", "Warcraft drone is going slow"]
    print("TEST TOYS: \(popularNToys(numToys: 6, topToys: 8, toys: toys, numQuotes: 4, quotes: quotes))")

}