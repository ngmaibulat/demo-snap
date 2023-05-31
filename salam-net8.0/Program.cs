using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Collections.ObjectModel;
// using EmptyCollections;

class Program
{
    record Person(string FirstName, string LastName);

    static void Main()
    {
        Action<string> printName = (string name) => Console.WriteLine(name);

        printName("Salam Aleikum!");

        var persons2 = Array.Empty<Person>();
        var persons = ReadOnlyCollection<Person>.Empty;
        // ReadOnlyDictionary<string, Person>.Empty;

        System.Console.WriteLine(persons.Count);
        System.Console.WriteLine(persons2.Length);
    }
}
