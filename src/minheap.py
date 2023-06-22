class minheap():

  def __init__(self) -> None:
    self.size = 0
    self.Heap = []

  def insert(self, rn, rc, td):
    err = "Duplicate RideNumber"
    ind = self.getIndex(rn)
    if ind != -1:
      return err
    self.Heap.append([rn, rc, td])
    i = len(self.Heap) - 1
    self.upHeapify(i)
    return None

  def getIndex(self, rn):
    for ind, trip in enumerate(self.Heap):
      if rn == trip[0]:
        return ind
    return -1

  def updateTrip(self, rn, newtd):
    ind = self.getIndex(rn)
    if newtd <= self.Heap[ind][2]:
      self.Heap[ind][2] = newtd
      self.upHeapify(ind)
      newind = self.getIndex(rn)
      self.downHeapify(newind)
    elif self.Heap[ind][2] < newtd <= 2 * self.Heap[ind][2]:
      temprn, temprc, _ = self.Heap[ind]
      self.Heap[ind][1] += 10
      self.Heap[ind][2] = newtd
      self.upHeapify(ind)
      newind = self.getIndex(rn)
      self.downHeapify(newind)
    elif newtd > 2 * self.Heap[ind][2]:
      self.cancelRide(rn)

  def cancelRide(self, rn):
    ind = self.getIndex(rn)
    if ind != -1:
      if ind == len(self.Heap) - 1:
        self.Heap.pop()
      else:
        self.Heap[ind] = self.Heap.pop()
        self.downHeapify(ind)

  def upHeapify(self, i):
    if i > 0 and (self.Heap[i][1] < self.Heap[(i - 1) // 2][1] or
                  (self.Heap[i][1] == self.Heap[(i - 1) // 2][1]
                   and self.Heap[i][2] < self.Heap[(i - 1) // 2][2])):
      self.Heap[i], self.Heap[(i - 1) // 2] = self.Heap[(i - 1) //
                                                        2], self.Heap[i]
      self.upHeapify((i - 1) // 2)

  def GetNextRide(self):
    if not self.Heap:
      return
    if len(self.Heap) == 1:
      ans = self.Heap.pop()
    else:
      ans = self.Heap[0]
      self.Heap[0] = self.Heap.pop()
      self.downHeapify(0)
    return ans

  def downHeapify(self, i):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if l < len(self.Heap) and ((self.Heap[l][1] < self.Heap[largest][1]) or
                               (self.Heap[l][1] == self.Heap[largest][1]
                                and self.Heap[l][2] < self.Heap[largest][2])):
      largest = l

    if r < len(self.Heap) and ((self.Heap[r][1] < self.Heap[largest][1]) or
                               (self.Heap[r][1] == self.Heap[largest][1]
                                and self.Heap[r][2] < self.Heap[largest][2])):
      largest = r
    if largest != i:
      self.Heap[i], self.Heap[largest] = self.Heap[largest], self.Heap[i]
      self.downHeapify(largest)
    return
