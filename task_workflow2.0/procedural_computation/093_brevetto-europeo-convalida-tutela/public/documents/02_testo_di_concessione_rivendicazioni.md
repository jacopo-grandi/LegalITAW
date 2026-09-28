EUROPEAN PATENT SPECIFICATION - EP 4 118 902 B1
Language of the proceedings: EN
Date of publication of the mention of the grant: see European Patent Bulletin
2026/05

Extract conserved on file: claims 1, 6, 7 and 12 as granted.

--------------------------------------------------------------------------------
CLAIMS
--------------------------------------------------------------------------------

1. An infusion device (10) comprising:
   a) a peristaltic pumping unit (12) arranged to deliver a fluid through a
      delivery line (14) at a commanded volumetric rate;
   b) a pressure transducer (16) arranged downstream of the pumping unit and
      configured to output a counter-pressure signal representative of the
      pressure in the delivery line;
   c) a control unit (18) configured to receive the counter-pressure signal and
      to modify the commanded volumetric rate as a function of a deviation
      between the counter-pressure signal and a reference profile;
   characterised in that the control unit (18) is further configured to update
   the reference profile during delivery on the basis of the counter-pressure
   signal acquired in a preceding time window, the update being performed
   without interrupting delivery.

6. The infusion device according to claim 1, wherein the preceding time window
   has a duration comprised between 20 and 240 seconds.

7. The infusion device according to claim 1, wherein the control unit (18) is
   configured to perform the update of the reference profile by means of a
   recursive estimator operating on the counter-pressure signal, the recursive
   estimator being selected among a recursive least squares estimator, a Kalman
   filter and a moving average estimator.

12. A method for regulating the delivery rate of an infusion device according to
    claim 1, comprising the steps of acquiring the counter-pressure signal,
    computing a deviation with respect to a reference profile, updating the
    reference profile on the basis of the counter-pressure signal acquired in a
    preceding time window and modifying the commanded volumetric rate as a
    function of the deviation, the updating step being performed without
    interrupting delivery.
