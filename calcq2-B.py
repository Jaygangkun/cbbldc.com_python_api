from flask import jsonify
import sys

class Calcq2:
    def calculate(self, in_logg, in_teff, in_logz, in_vel):
        file = open('LDCQ2.txt', 'r')
        
        xin_logg = float('100000')
        if in_logg < 0.00:
            return jsonify({'success': False, 'message': 'log(g) value out of range'})
        elif in_logg >= 0.00 and in_logg < 0.25:
            xin_logg = 0.00
        elif in_logg >= 0.25 and in_logg < 0.75:
            xin_logg = 0.50
        elif in_logg >= 0.75 and in_logg < 1.25:
            xin_logg = 1.00
        elif in_logg >= 1.25 and in_logg < 1.75:
            xin_logg = 1.50
        elif in_logg >= 1.75 and in_logg < 2.25:
            xin_logg = 2.00
        elif in_logg >= 2.25 and in_logg < 2.75:
            xin_logg = 2.50
        elif in_logg >= 2.75 and in_logg < 3.25:
            xin_logg = 3.00
        elif in_logg >= 3.25 and in_logg < 3.75:
            xin_logg = 3.50
        elif in_logg >= 3.75 and in_logg < 4.25:
            xin_logg = 4.00
        elif in_logg >= 4.25 and in_logg < 4.75:
            xin_logg = 4.50
        elif in_logg >= 4.75 and in_logg <= 5.00:
            xin_logg = 5.00
        elif in_logg > 5.00:
            return jsonify({'success': False, 'message': 'log(g) value out of range'})

        # Correct Teff input

        xin_teff = float('100000')
        if in_teff < 3500:
            return jsonify({'success': False, 'message': 'Teff value out of range'})
        elif in_teff >= 3500 and in_teff < 3625:
            xin_teff = 3500    
        elif in_teff >= 3625 and in_teff < 3875:
            xin_teff = 3750
        elif in_teff >= 3875 and in_teff < 4125:
            xin_teff = 4000
        elif in_teff >= 4125 and in_teff < 4375:
            xin_teff = 4250
        elif in_teff >= 4375 and in_teff < 4625:
            xin_teff = 4500                                 
        elif in_teff >= 4625 and in_teff < 4875:
            xin_teff = 4750
        elif in_teff >= 4875 and in_teff < 5125:
            xin_teff = 5000
        elif in_teff >= 5125 and in_teff < 5375:
            xin_teff = 5250
        elif in_teff >= 5375 and in_teff < 5625:
            xin_teff = 5500
        elif in_teff >= 5625 and in_teff < 5875:
            xin_teff = 5750
        elif in_teff >= 5875 and in_teff < 6125:
            xin_teff = 6000
        elif in_teff >= 6125 and in_teff < 6375:
            xin_teff = 6250
        elif in_teff >= 6375 and in_teff < 6625:
            xin_teff = 6500
        elif in_teff >= 6625 and in_teff < 6875:
            xin_teff = 6750
        elif in_teff >= 6875 and in_teff < 7125:
            xin_teff = 7000
        elif in_teff >= 7125 and in_teff < 7375:
            xin_teff = 7250
        elif in_teff >= 7375 and in_teff < 7625:
            xin_teff = 7500
        elif in_teff >= 7625 and in_teff < 7875:
            xin_teff = 7750
        elif in_teff >= 7875 and in_teff < 8125:
            xin_teff = 8000
        elif in_teff >= 8125 and in_teff < 8375:
            xin_teff = 8250
        elif in_teff >= 8375 and in_teff < 8625:
            xin_teff = 8500
        elif in_teff >= 8625 and in_teff < 8875:
            xin_teff = 8750
        elif in_teff >= 8875 and in_teff < 9125:
            xin_teff = 9000
        elif in_teff >= 9125 and in_teff < 9375:
            xin_teff = 9250
        elif in_teff >= 9375 and in_teff < 9625:
            xin_teff = 9500
        elif in_teff >= 9625 and in_teff < 9875:
            xin_teff = 9750
        elif in_teff >= 9875 and in_teff < 10125:
            xin_teff = 10000
        elif in_teff >= 10125 and in_teff < 10750:
            xin_teff = 10500
        elif in_teff >= 10750 and in_teff < 11250:
            xin_teff = 11000
        elif in_teff >= 11250 and in_teff < 11750:
            xin_teff = 11500                               
        elif in_teff >= 11750 and in_teff < 12250:
            xin_teff = 12000
        elif in_teff >= 12250 and in_teff < 12750:
            xin_teff = 12500
        elif in_teff >= 12750 and in_teff < 13250:
            xin_teff = 13000    
        elif in_teff >= 13250 and in_teff < 14500:
            xin_teff = 14000
        elif in_teff >= 14500 and in_teff < 15500:
            xin_teff = 15000
        elif in_teff >= 15500 and in_teff < 16500:
            xin_teff = 16000
        elif in_teff >= 16500 and in_teff < 17500:
            xin_teff = 17000
        elif in_teff >= 17500 and in_teff < 18500:
            xin_teff = 18000
        elif in_teff >= 18500 and in_teff < 19500:
            xin_teff = 19000
        elif in_teff >= 19500 and in_teff < 20500:
            xin_teff = 20000
        elif in_teff >= 20500 and in_teff < 21500:
            xin_teff = 21000
        elif in_teff >= 21500 and in_teff < 22500:
            xin_teff = 22000
        elif in_teff >= 22500 and in_teff < 23500:
            xin_teff = 23000
        elif in_teff >= 23500 and in_teff < 24500:
            xin_teff = 24000
        elif in_teff >= 24500 and in_teff < 25500:
            xin_teff = 25000
        elif in_teff >= 25500 and in_teff < 26500:
            xin_teff = 26000
        elif in_teff >= 26500 and in_teff < 27500:
            xin_teff = 27000
        elif in_teff >= 27500 and in_teff < 28500:
            xin_teff = 28000
        elif in_teff >= 28500 and in_teff < 29500:
            xin_teff = 29000
        elif in_teff >= 29500 and in_teff < 30500:
            xin_teff = 30000
        elif in_teff >= 30500 and in_teff < 31500:
            xin_teff = 31000
        elif in_teff >= 31500 and in_teff < 32500:
            xin_teff = 32000
        elif in_teff >= 32500 and in_teff < 33500:
            xin_teff = 33000
        elif in_teff >= 33500 and in_teff < 34500:
            xin_teff = 34000
        elif in_teff >= 34500 and in_teff < 35500:
            xin_teff = 35000                              
        elif in_teff >= 35500 and in_teff < 36500:
            xin_teff = 37500
        elif in_teff >= 36500 and in_teff < 41000:
            xin_teff = 40000
        elif in_teff >= 41000 and in_teff < 44000:
            xin_teff = 42500
        elif in_teff >= 44000 and in_teff < 46000:
            xin_teff = 45000
        elif in_teff >= 46000 and in_teff < 48250:
            xin_teff = 47500
        elif in_teff >= 48250 and in_teff <= 50000:
            xin_teff = 50000
        elif in_teff > 50000:
            return jsonify({'success': False, 'message': 'Teff value out of range'})
            
        # Correct logz input

        xin_logz = float('200000')
        if in_logz < -5.0:
            return jsonify({'success': False, 'message': '[Fe/H] value out of range'})
        elif in_logz >= -5.0 and in_logz < -4.7:
            xin_logz = -5.0
        elif in_logz >= -4.7 and in_logz < -4.2:
            xin_logz = -4.5
        elif in_logz >= -4.2 and in_logz < -3.7:
            xin_logz = -4.0
        elif in_logz >= -3.7 and in_logz < -3.2:
            xin_logz = -3.5
        elif in_logz >= -3.2 and in_logz < -2.7:
            xin_logz = -3.0
        elif in_logz >= -2.7 and in_logz < -2.2:
            xin_logz = -2.5
        elif in_logz >= -2.2 and in_logz < -1.7:
            xin_logz = -2.0
        elif in_logz >= -1.7 and in_logz < -1.2:
            xin_logz = -1.5
        elif in_logz >= -1.2 and in_logz < -0.7:
            xin_logz = -1.0
        elif in_logz >= -0.7 and in_logz < -0.3:
            xin_logz = -0.5
        elif in_logz >= -0.3 and in_logz < -0.2:
            xin_logz = -0.3
        elif in_logz >= -0.2 and in_logz < -0.1:
            xin_logz = -0.2
        elif in_logz >= -0.1 and in_logz < 0.0:
            xin_logz = -0.1
        elif in_logz >= 0.0 and in_logz < 0.1:
            xin_logz = 0.0
        elif in_logz >= 0.1 and in_logz < 0.2:
            xin_logz = 0.1                            
        elif in_logz >= 0.2 and in_logz < 0.3:
            xin_logz = 0.2
        elif in_logz >= 0.3 and in_logz < 0.5:
            xin_logz = 0.3
        elif in_logz >= 0.5 and in_logz < 0.8:
            xin_logz = 0.5
        elif in_logz >= 0.8 and in_logz <= 1.0:
            xin_logz = 1.0
        elif in_logz > 1.0:
            return jsonify({'success': False, 'message': '[Fe/H] value out of range'})

        #@@@ Correct vel input

        xin_vel = float('100000')             
        if in_vel < 0.00:
            return jsonify({'success': False, 'message': 'vel value out of range'})
        elif in_vel >= 0.00 and in_vel < 0.50:
            xin_vel = 0.00
        elif in_vel >= 0.50 and in_vel < 1.50:
            xin_vel = 1.00
        elif in_vel >= 1.50 and in_vel < 3.00:
            xin_vel = 2.00
        elif in_vel >= 3.00 and in_vel < 6.00:
            xin_vel = 4.00
        elif in_vel >= 6.00 and in_vel <= 8.00:
            xin_vel = 8.00
        elif in_vel > 8.00:
            return jsonify({'success': False, 'message': 'vel value out of range'})

        # Get rid of the headers:

        read_line = file.readline()
        read_line = file.readline()
        read_line = file.readline()

        #=============================== START LOOP 1 (Get log(g) ==========================================

        a = 9000000000
        i = 1
        AA_Alogg = -6.00

        while i < a:
            
        # Read Next Line of data
        
            read_line = file.readline()

        # Split fields and assign

            fields = read_line.strip().split()
            Alogg = float(fields[0])
            Ateff = float(fields[1])
            Alogz = float(fields[2])
            Avel = float(fields[3])  # CHANGED
            Aa1a = float(fields[4])

        # Read Line 2 of data:

            read_line = file.readline()
            
        # Split fields and assign

            fields = read_line.strip().split()
            Blogg = float(fields[0])
            Bteff = float(fields[1])
            Blogz = float(fields[2])
            Bvel = float(fields[3])  # CHANGED
            Ba1b = float(fields[4])

        # Get rid of the Error Line :

            read_line = file.readline()
            if not read_line:
                print("Record could not be found")
                break

            if xin_logg == Alogg:
                AA_Alogg = Alogg
                break
                a = a-1

        #================================= Start LOOP 2 (Get Teff) ======================== :
                
        file.seek(0)

        # Get rid of the headers

        read_line = file.readline()
        read_line = file.readline()
        read_line = file.readline()

        a2 = 9000000000
        i2 = 1
        AA_Ateff = -6.00

        while i2 < a2:
            
        # Read Next Line of data

            read_line = file.readline()
                
        # Split fields and assign

            fields = read_line.strip().split()
            Alogg = float(fields[0])
            Ateff = float(fields[1])
            Alogz = float(fields[2])
            Avel = float(fields[3])  # CHANGED
            Aa1a = float(fields[4])
            
        # Read Line 2 of data:

            read_line = file.readline()
            
        # Split fields and assign

            fields = read_line.strip().split()
            Blogg = float(fields[0])
            Bteff = float(fields[1])
            Blogz = float(fields[2])
            Bvel = float(fields[3])  # CHANGED
            Ba1b = float(fields[4])

        # Get rid of the Error Line

            read_line = file.readline()
            if not read_line:
                print("Record could not be found")
                break

            if xin_teff == Ateff:
                AA_Ateff = Ateff
                break
                a2 = a2-1

        #================================= Start LOOP 3 (Get log(z)) ========================
                
        file.seek(0)

        # Get rid of the headers

        read_line = file.readline()
        read_line = file.readline()
        read_line = file.readline()

        a3 = 9000000000
        i3 = 1
        AA_Alogz = -6.00

        while i3 < a3:
            
            
        # Read Next Line of data

            read_line = file.readline()
                    
        # Split fields and assign
            
            fields = read_line.strip().split()
            Elogg = float(fields[0])
            Eteff = float(fields[1])
            Elogz = float(fields[2])
            Evel = float(fields[3])  # CHANGED
            Ea1a = float(fields[4])
            
        # Read Line 2 of data 

            read_line = file.readline()
            
        # Split fields and assign

            fields = read_line.strip().split()
            Glogg = float(fields[0])
            Gteff = float(fields[1])
            Glogz = float(fields[2])
            Gvel = float(fields[3])  # CHANGED
            Ga1b = float(fields[4])

        # Get rid of the Error Line 

            read_line = file.readline()
            if not read_line:
                print("Record could not be found")
                break

            if xin_logz == Elogz:
                AA_Alogz = Elogz
                break
                a3 = a3-1

        #================================= Start LOOP 4 (Get vel) ========================  # ADDED
                
        file.seek(0)

        # Get rid of the headers

        read_line = file.readline()
        read_line = file.readline()
        read_line = file.readline()

        a4 = 9000000000
        i4 = 1
        AA_Avel = -6.00

        while i4 < a4:
            
            
        # Read Next Line of data

            read_line = file.readline()
                    
        # Split fields and assign
            
            fields = read_line.strip().split()
            Elogg = float(fields[0])
            Eteff = float(fields[1])
            Elogz = float(fields[2])
            Evel = float(fields[3])
            Ea1a = float(fields[4])
            
        # Read Line 2 of data 

            read_line = file.readline()
            
        # Split fields and assign

            fields = read_line.strip().split()
            Glogg = float(fields[0])
            Gteff = float(fields[1])
            Glogz = float(fields[2])
            Gvel = float(fields[3])
            Ga1b = float(fields[4])

        # Get rid of the Error Line 

            read_line = file.readline()
            if not read_line:
                print("Record could not be found")
                break

            if xin_vel == Evel:
                AA_Avel = Evel
                break
                a4 = a4-1

        #==================================== Find correct record =====================

        file.seek(0)

        # Get rid of the headers

        read_line = file.readline()
        read_line = file.readline()
        read_line = file.readline()

        a5 = 9000000000  # CHANGED
        i5 = 1           # CHANGED
        
        while i5 < a5:
            
        # Read Next Line of data

            try:
                read_line = file.readline()
            except:
                return jsonify({'success': False, 'message': 'No coefficients exist for input values'})
                
        # Split fields and assign
            try:
                fields = read_line.strip().split()
            except:
                return jsonify({'success': False, 'message': 'No coefficients exist for input values'})
            try:
                Ylogg = float(fields[0])
            except:
                return jsonify({'success': False, 'message': 'No coefficients exist for input values'})
            try:
                Yteff = float(fields[1])
            except:
                return jsonify({'success': False, 'message': 'No coefficients exist for input values'})
            try:
                Ylogz = float(fields[2])
            except:
                return jsonify({'success': False, 'message': 'No coefficients exist for input values'})
            try:
                Yvel = float(fields[3])  # CHANGED
            except:
                return jsonify({'success': False, 'message': 'No coefficients exist for input values'})
            try:
                Ya1a = float(fields[4])
            except:
                return jsonify({'success': False, 'message': 'No coefficients exist for input values'})
            
            if Ylogg == AA_Alogg and Yteff == AA_Ateff and Ylogz == AA_Alogz and Yvel == AA_vel:
                read_line = file.readline()
                fields = read_line.strip().split()
                Zlogg = float(fields[0])
                Zteff = float(fields[1])
                Zlogz = float(fields[2])
                Zvel = float(fields[3])
                Za1a = float(fields[4])
                
                a5 = a5-1
                
                return jsonify({'success': True, 'u1': Ya1a, 'u2': Za1a})
        
        return jsonify({'success': False})
