# OOD

```
String[] a = {“1,0.49,Candy”, “2,1.49,Bread” };
```
to list

```
List<Item> list = Arrays.asList(arr).stream().map(Item::new).collect(Collectors.toList());
```

to map
```
Map<Integer, String> list = Arrays.asList(arr).stream().map(Item::new).sorted().collect(Collectors.toMap(Item::getId, Item::getName));
```

ConvertUtil.strToIntStatic()

Arrays.asList(arr).stream().boxed().sorted().collect(Collectors.toList())