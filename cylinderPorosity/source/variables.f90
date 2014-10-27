module variables


implicit none

integer :: i,j,k,l ! Loop
integer :: mi1, mi2, mo1
double precision, allocatable, dimension (:) :: x,y,z,r
double precision, allocatable, dimension(:,:) :: poro
real*8 :: totaltime,rcmin,rcmax,rcstep,rc,rs,x0,y0,z0,angle1,angle2,angle,anglebis
real*8 :: htot,zite,themax,t,rzmax,zmax,surfaceintersect
integer*8 :: Ntot,Nite,nbreplan,nbreinteg,datafilel,counting
double precision, allocatable, dimension(:) :: ztemp

real*8, parameter :: pi=3.14159

character(len=80) :: filename,datafile
end module variables
