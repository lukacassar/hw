(** Question 1.
    [is_even x] returns true if [x] is even, otherwise false.
*)
let is_even (x : int): bool =
  if (x mod 2 = 0) then true else false;;

(** Question 2.
  [remove_int l n] removes every occurrence of [n] from [l].
*)
let rec remove_int (l: int list) (n: int) =
  match l with
  h::t -> if (h = n) then remove_int t n else h :: remove_int t n
  | [] -> l;;

(** Question 3.
  [sum l] returns the summation of the elements of [l].
*)
let rec sum (l : int list): int =
  let rec sum_helper l acc = 
    match l with
    h::t -> sum_helper t (acc+h) 
    | [] -> acc
  in
  sum_helper l 0;;
  
(** Question 4.
  [rev l] reverses the elements of [l].
*)
let rev (l : 'a list) : 'a list =
  let rec rev_helper l acc = 
    match l with
      h::t -> rev_helper t (h::acc)
    | [] -> acc 
  in
  rev_helper l [];;

(** Question 5.
  [even_sized_palindrome l] returns the even-sized palindrome of [l].

  Length of result is 2 * [l].
*)
let even_sized_palindrome (l: 'a list): 'a list  =
  l @ rev l;;

(** Question 6.
  [is_palindrome l] returns true if [l] is a palindrome, otherwise false.
*)
let is_palindrome (l: 'a list): bool =
  if l = rev l then true else false;;