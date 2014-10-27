
!_____________________________________________

      include "variables.f90"

      program cylinderpore3ds

      use variables
!____________________________________________


open(unit=mi1, file="cylinderpore3ds.tmp")
rewind mi1

read(mi1,*)
read(mi1,*) datafile
read(mi1,*)
read(mi1,*) nbreplan
read(mi1,*)
read(mi1,*) nbreinteg

close(mi1)

datafilel=len_trim(datafile)

write (filename, "(A,I1)") datafile(1:datafilel),0
open(unit=mi2, file=filename)
rewind mi2

read(mi2,*) Nite
read(mi2,*) htot
read(mi2,*) rcmin
read(mi2,*) rcmax
read(mi2,*) Ntot
read(mi2,*) t
read(mi2,*)

close(mi2)


allocate(x(Ntot),y(Ntot),z(Ntot),r(Ntot),ztemp(Ntot),poro(nbreplan,Nite+1))


do l=1, nbreplan
	poro(l,1)=rcmin+(l-1)*(rcmax-rcmin)/(nbreplan-1)
end do

print *, "fichier: ", datafile(1:datafilel), filename
do i=1,Nite
!Open file ( 1 to 9, 10 to 99 etc...)
! read data
	if (i<11) then
		write (filename, "(A,I1)") datafile(1:datafilel),i-1
	elseif ((i>=11) .and. (i<101) ) then
		write (filename, "(A,I2)") datafile(1:datafilel),i-1
	else
		write (filename, "(A,I3)") datafile(1:datafilel),i-1
	endif 

	open(unit=mi2, file=filename)
	rewind mi2
	print *, filename, "is open"


	read(mi2,*) Nite
	read(mi2,*) htot
	read(mi2,*) rcmin
	read(mi2,*) rcmax
	read(mi2,*) Ntot
	read(mi2,*) t
	read(mi2,*)

	do k=1,Ntot
		read(mi2,*) x(k),y(k),z(k),r(k)
		x(k)=sqrt((x(k))**2+(y(k))**2)
		y(k)=0
	end do
	close(mi2)

	do j=1,nbreplan
		poro(j,i+1)=0
		rc=poro(j,1)
                surfaceintersect=.0 ! Initialization of the value after each calculation

		do k=1,Ntot
			if ((rc>x(k)-0.97*r(k)) .and. (rc<x(k)+0.97*r(k))) then !Condition croisement sphere et cylindre
				rzmax=abs(rc-x(k))
				zmax=sqrt(r(k)**2-rzmax**2)
				deltaz=zmax/dble(nbreinteg)

				! Initialization of trapezoidal rule with middle sphere angle 
				call theta(x(k),y(k),z(k),z(k),rc,r(k),anglebis)

				do l=1,nbreinteg

					zite=0.97*dble(l)*deltaz
					call theta(x(k),y(k),z(k),z(k)+zite,rc,r(k),angle)
					surfaceintersect=surfaceintersect+(angle+anglebis)*rc*deltaz !
					anglebis=angle

				end do
			end if
		end do

		poro(j,i+1)=1-(surfaceintersect/(2*pi*rc*htot))
	end do
end do

2100 format(50000(e13.8,3x))

open(unit=mo1, file=datafile(1:datafilel)//"Results")
write(mo1,*) "Number of plans"
write(mo1,*) nbreplan
write(mo1,*) "Number of particles"
write(mo1,*) Ntot
write(mo1,*) "Number of iterations"
write(mo1,*) Nite
write(mo1,*) "By column order: cylinder size - porosity iter 1 - porosity iter 2 - etc...."
write(mo1,*) "***********************"

do i=1,nbreplan
	write(mo1,2100) (real(real(poro(i,j))),j=1,1+Nite) 
end do
close(mo1)

end program

! Subroutine theta
Subroutine theta(x0,y0,z0,z,rc,rs,angle)

     double precision, intent(in) :: x0,y0,z0,z,rc,rs
     double precision, intent(out) :: angle
     double precision :: angle1,angle2
     angle1= -acos(1/((2*rc**2*(x0**2 + y0**2))/ &
     &  (rc**3*x0 + rc*x0*(-rs**2 + x0**2 + y0**2 + (z - z0)**2) - &
     &  sqrt(-(rc**2*y0**2* &
     &  (rc**4 + (-rs**2 + x0**2 + y0**2 + (z - z0)**2)**2 - &
     &  2*rc**2*(rs**2 + x0**2 + (y0 + z - z0)*(y0 - z + z0))))))))

     angle2=acos(1/((2*rc**2*(x0**2 + y0**2))/ &
     &   (rc**3*x0 + rc*x0*(-rs**2 + x0**2 + y0**2 + (z - z0)**2) - &
     &    sqrt(-(rc**2*y0**2* &
     &   (rc**4 + (-rs**2 + x0**2 + y0**2 + (z - z0)**2)**2 - &
     &   2*rc**2*(rs**2 + x0**2 + (y0 + z - z0)*(y0 - z + z0))))))))

     angle=abs(real(real(angle1))-real(real(angle2)))
!print *, x0,y0,z0,z0,z,rs,angle

end
