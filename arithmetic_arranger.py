def arithmetic_arranger(problems, wantans=False):
  count = 0
  arranged_problems = ''
  fline = ''
  sline = ''
  hashline = ''
  ansline = ''
  splitproblems = list()
  # format error checking
  allowed = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '+', '-']
  for problem in problems :
    if count > 4 :
      return('Error: Too many problems.')
      quit()
    if '+' in problem :
      count = count + 1
    elif '-' in problem :
      count = count + 1
    else :
      return('Error: Operator must be \'+\' or \'-\'.')
      quit()  
    for dig in problem :
      if dig not in allowed :
        return('Error: Numbers must only contain digits.')
        quit()
    indivnums = problem.split()
    for num in indivnums :
      if len(num) > 4 :
        return('Error: Numbers cannot be more than four digits.')
        quit()
  # end format error checking

  for problem in problems :
    splitproblem = problem.split()
    splitproblems.append(splitproblem)
    splitproblem[0] = int(splitproblem[0])
    splitproblem[2] = int(splitproblem[2])
    if splitproblem[1] == '+' :
      ans = splitproblem[0] + splitproblem[2]
    if splitproblem[1] == '-' :
      ans = splitproblem[0] - splitproblem[2]
    splitproblem.append(ans)
    
  for problem in splitproblems :
    problem[0] = str(problem[0])
    problem[2] = str(problem[2])
    problem[3] = str(problem[3])
    if len(problem[0]) < len(problem[2]) :
      tspaces = len(problem[2]) - len(problem[0]) + 2
      bspaces = 1
    elif len(problem[0]) > len(problem[2]) :
      tspaces = 2
      bspaces = len(problem[0]) - len(problem[2]) + 1
    else :
      tspaces = 2
      bspaces = 1
    for i in range(tspaces) :
      problem[0] = ' ' + problem[0]
    for i in range(bspaces) :
      problem[2] = ' ' + problem[2]
    hashnum = len(problem[0])
    aspaces = hashnum - len(problem[3])
    hashes = ''
    for i in range(hashnum) :
      hashes = hashes + '-'
    for i in range(aspaces) :
      problem[3] = ' ' + problem[3]
    problem[2] = problem[1] + problem[2] + '    '
    problem[0] = problem[0] + '    '
    problem[3] = problem[3] + '    '
    hashes = hashes + '    '
    fline = fline + problem[0]
    sline = sline + problem[2]
    hashline = hashline + hashes
    ansline = ansline + problem[3]

  fline = fline.rstrip() + '\n'
  sline = sline.rstrip() + '\n'
  hashline = hashline.rstrip()
  ansline = ansline.rstrip()
  if wantans == True :
    hashline = hashline + '\n'
    arranged_problems = fline + sline + hashline + ansline
  else :
    arranged_problems = fline + sline + hashline
  return arranged_problems
