      SUBROUTINE NUMBER_HISTOGRAM(A,N,BADDATA,BIN_MIN,BIN_INC,N_BINS,
     $NUMBER_HIST,N_TOT)

C  Thomas Matejka NOAA/NSSL 15 July 1996

      IMPLICIT NONE
      INTEGER::N,I,N_TOT,N_BINS,I_BIN
      INTEGER,DIMENSION(N_BINS)::NUMBER_HIST
      REAL::BADDATA,BIN_MIN,BIN_INC
      REAL,DIMENSION(N)::A

      N_TOT=0
      DO I_BIN=1,N_BINS
         NUMBER_HIST(I_BIN)=0
      ENDDO
      DO I=1,N
         IF(A(I).NE.BADDATA)THEN
            N_TOT=N_TOT+1
            I_BIN=IFIX((A(I)-BIN_MIN)/BIN_INC)+1
            IF(I_BIN.GE.1.AND.
     $      I_BIN.LE.N_BINS)THEN
               NUMBER_HIST(I_BIN)=NUMBER_HIST(I_BIN)+1
            ENDIF
         ENDIF
      ENDDO
      END