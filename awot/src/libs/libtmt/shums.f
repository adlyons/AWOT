      REAL FUNCTION SHUMS(T,P)

C  Thomas Matejka NOAA/NSSL 10 March 1993

      IMPLICIT NONE
      INCLUDE 'include_constants.inc'
      INCLUDE 'tmtlib.inc'
      REAL VAPPS
      REAL T,P,ES

      ES=VAPPS(T)
      IF(ES.GE.P)THEN
         WRITE(TMTLIB_MESSAGE_UNIT,*)'SHUMS:  ES IS GREATER THAN OR ',
     $   'EQUAL TO P.'
         STOP
      ENDIF
      SHUMS=ES*MW_H2O/((P-ES)*MW_DRY+ES*MW_H2O)
      RETURN
      END
