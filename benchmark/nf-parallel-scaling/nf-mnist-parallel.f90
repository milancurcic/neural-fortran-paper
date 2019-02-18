program example_mnist

  ! A training example with the MNIST dataset.
  ! Uses stochastic gradient descent and mini-batch size of 100.
  ! Can be run in serial or parallel mode without modifications.

  use mod_kinds, only: ik, rk
  use mod_mnist, only: label_digits, load_mnist
  use mod_network, only: network_type

  implicit none

  real(rk), allocatable :: tr_images(:,:), tr_labels(:)
  real(rk), allocatable :: te_images(:,:), te_labels(:)
  real(rk), allocatable :: va_images(:,:), va_labels(:)
  real(rk), allocatable :: input(:,:), output(:,:)

  type(network_type) :: net

  integer(ik) :: i, n, num_epochs
  integer(ik) :: batch_size, batch_start, batch_end
  real(rk) :: pos
  real(rk) :: t0, t1

  call load_mnist(tr_images, tr_labels, te_images,&
                  te_labels, va_images, va_labels)

  net = network_type([784, 30, 10])

  batch_size = 1200
  num_epochs = 10

  if (this_image() == 1) call cpu_time(t0)

  epochs: do n = 1, num_epochs
    mini_batches: do i = 1, size(tr_labels) / batch_size

      ! pull a random mini-batch from the dataset
      call random_number(pos)
      batch_start = int(pos * (size(tr_labels) - batch_size + 1))
      batch_end = batch_start + batch_size - 1

      ! prepare mini-batch
      input = tr_images(:,batch_start:batch_end)
      output = label_digits(tr_labels(batch_start:batch_end))

      ! train the network on the mini-batch
      call net % train(input, output, eta=3._rk)

    end do mini_batches

  end do epochs

  if (this_image() == 1) then
    call cpu_time(t1)
    print *, num_images(), t1 - t0
  end if

end program example_mnist
