letters=[['    *    ', '**** ', ' *****', '*****  ', '******', '******', '******', '*    *', '*****', '*****', '*   *', '*    ', '*   *', '*   *', '  **  ', '**** ', '  **   ', '**** ', '******', '*****', '*    *', '*       *', '*   *    *', '*     *', '*     *', '******'], 
         ['   * *   ', '*   *', '*     ', '*    * ', '*     ', '*     ', '*     ', '*    *', '  *  ', '  *  ', '*  * ', '*    ', '** **', '**  *', '*    *', '*   *', '*    * ', '*   *', '*    *', '  *  ', '*    *', ' *     * ', '*   *    *', '  * *  ', '  * *  ', '    * '], 
         ['  *   *  ', '**** ', '*     ', '*     *', '***** ', '***** ', '*   **', '******', '  *  ', '  *  ', '**   ', '*    ', '* * *', '* * *', '*    *', '**** ', '*  * * ', '**** ', '   *  ', '  *  ', '*    *', '  *   *  ', '*   *    *', '   *   ', '   *   ', '   *  '], 
         [' * * * * ', '*   *', '*     ', '*    * ', '*     ', '*     ', '*    *', '*    *', '  *  ', '* *  ', '*  * ', '*    ', '*   *', '*  **', '*    *', '*    ', '*    * ', '* *  ', '*    *', '  *  ', '*    *', '   * *   ', '*   *    *', '  * *  ', '  *    ', ' *    '], 
         ['*       *', '**** ', ' *****', '*****  ', '******', '*     ', '******', '*    *', '*****', '**   ', '*   *', '*****', '*   *', '*   *', '  **  ', '*    ', '  **  *', '*  * ', '******', '  *  ', '  **  ', '    *    ', '  *   *   ', '*     *', '*      ', '******']]

str = input("Enter something:").upper()
to_num= list(ord(x)-ord("A") for x in str)
p,a=[],[""]*5
for x in to_num:
    for y in range(5) : a[y] += letters[y][x]+"  "
for x in a:print(x)