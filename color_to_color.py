import sublime, sublime_plugin, math, re
class color_to_color(sublime_plugin.TextCommand):
	colors = {"name": ["aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "black", "blanchedalmond", "blue", "blueviolet", "brown", "burlywood", "cadetblue", "chartreuse", "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson", "cyan", "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen", "darkgrey", "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray", "darkslategrey", "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", "dimgrey", "dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia", "gainsboro", "ghostwhite", "gold", "goldenrod", "gray", "green", "greenyellow", "grey", "honeydew", "hotpink", "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgray", "lightgreen", "lightgrey", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightslategrey", "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon", "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite", "navy", "oldlace", "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum", "powderblue", "purple", "red", "rosybrown", "royalblue", "saddlebrown", "salmon", "sandybrown", "seagreen", "seashell", "sienna", "silver", "skyblue", "slateblue", "slategray", "slategrey", "snow", "springgreen", "steelblue", "tan", "teal", "thistle", "tomato", "turquoise", "violet", "wheat", "white", "whitesmoke", "yellow", "yellowgreen"], "hex": ["f0f8ff", "faebd7", "00ffff", "7fffd4", "f0ffff", "f5f5dc", "ffe4c4", "000000", "ffebcd", "0000ff", "8a2be2", "a52a2a", "deb887", "5f9ea0", "7fff00", "d2691e", "ff7f50", "6495ed", "fff8dc", "dc143c", "00ffff", "00008b", "008b8b", "b8860b", "a9a9a9", "006400", "a9a9a9", "bdb76b", "8b008b", "556b2f", "ff8c00", "9932cc", "8b0000", "e9967a", "8fbc8f", "483d8b", "2f4f4f", "2f4f4f", "00ced1", "9400d3", "ff1493", "00bfff", "696969", "696969", "1e90ff", "b22222", "fffaf0", "228b22", "ff00ff", "dcdcdc", "f8f8ff", "ffd700", "daa520", "808080", "008000", "adff2f", "808080", "f0fff0", "ff69b4", "cd5c5c", "4b0082", "fffff0", "f0e68c", "e6e6fa", "fff0f5", "7cfc00", "fffacd", "add8e6", "f08080", "e0ffff", "fafad2", "d3d3d3", "90ee90", "d3d3d3", "ffb6c1", "ffa07a", "20b2aa", "87cefa", "778899", "778899", "b0c4de", "ffffe0", "00ff00", "32cd32", "faf0e6", "ff00ff", "800000", "66cdaa", "0000cd", "ba55d3", "9370db", "3cb371", "7b68ee", "00fa9a", "48d1cc", "c71585", "191970", "f5fffa", "ffe4e1", "ffe4b5", "ffdead", "000080", "fdf5e6", "808000", "6b8e23", "ffa500", "ff4500", "da70d6", "eee8aa", "98fb98", "afeeee", "db7093", "ffefd5", "ffdab9", "cd853f", "ffc0cb", "dda0dd", "b0e0e6", "800080", "ff0000", "bc8f8f", "4169e1", "8b4513", "fa8072", "f4a460", "2e8b57", "fff5ee", "a0522d", "c0c0c0", "87ceeb", "6a5acd", "708090", "708090", "fffafa", "00ff7f", "4682b4", "d2b48c", "008080", "d8bfd8", "ff6347", "40e0d0", "ee82ee", "f5deb3", "ffffff", "f5f5f5", "ffff00", "9acd32"], "rgb": [[240, 248, 255 ], [250, 235, 215 ], [0, 255, 255 ], [127, 255, 212 ], [240, 255, 255 ], [245, 245, 220 ], [255, 228, 196 ], [0, 0, 0 ], [255, 235, 205 ], [0, 0, 255 ], [138, 43, 226 ], [165, 42, 42 ], [222, 184, 135 ], [95, 158, 160 ], [127, 255, 0 ], [210, 105, 30 ], [255, 127, 80 ], [100, 149, 237 ], [255, 248, 220 ], [220, 20, 60 ], [0, 255, 255 ], [0, 0, 139 ], [0, 139, 139 ], [184, 134, 11 ], [169, 169, 169 ], [0, 100, 0 ], [169, 169, 169 ], [189, 183, 107 ], [139, 0, 139 ], [85, 107, 47 ], [255, 140, 0 ], [153, 50, 204 ], [139, 0, 0 ], [233, 150, 122 ], [143, 188, 143 ], [72, 61, 139 ], [47, 79, 79 ], [47, 79, 79 ], [0, 206, 209 ], [148, 0, 211 ], [255, 20, 147 ], [0, 191, 255 ], [105, 105, 105 ], [105, 105, 105 ], [30, 144, 255 ], [178, 34, 34 ], [255, 250, 240 ], [34, 139, 34 ], [255, 0, 255 ], [220, 220, 220 ], [248, 248, 255 ], [255, 215, 0 ], [218, 165, 32 ], [128, 128, 128 ], [0, 128, 0 ], [173, 255, 47 ], [128, 128, 128 ], [240, 255, 240 ], [255, 105, 180 ], [205, 92, 92 ], [75, 0, 130 ], [255, 255, 240 ], [240, 230, 140 ], [230, 230, 250 ], [255, 240, 245 ], [124, 252, 0 ], [255, 250, 205 ], [173, 216, 230 ], [240, 128, 128 ], [224, 255, 255 ], [250, 250, 210 ], [211, 211, 211 ], [144, 238, 144 ], [211, 211, 211 ], [255, 182, 193 ], [255, 160, 122 ], [32, 178, 170 ], [135, 206, 250 ], [119, 136, 153 ], [119, 136, 153 ], [176, 196, 222 ], [255, 255, 224 ], [0, 255, 0 ], [50, 205, 50 ], [250, 240, 230 ], [255, 0, 255 ], [128, 0, 0 ], [102, 205, 170 ], [0, 0, 205 ], [186, 85, 211 ], [147, 112, 219 ], [60, 179, 113 ], [123, 104, 238 ], [0, 250, 154 ], [72, 209, 204 ], [199, 21, 133 ], [25, 25, 112 ], [245, 255, 250 ], [255, 228, 225 ], [255, 228, 181 ], [255, 222, 173 ], [0, 0, 128 ], [253, 245, 230 ], [128, 128, 0 ], [107, 142, 35 ], [255, 165, 0 ], [255, 69, 0 ], [218, 112, 214 ], [238, 232, 170 ], [152, 251, 152 ], [175, 238, 238 ], [219, 112, 147 ], [255, 239, 213 ], [255, 218, 185 ], [205, 133, 63 ], [255, 192, 203 ], [221, 160, 221 ], [176, 224, 230 ], [128, 0, 128 ], [255, 0, 0 ], [188, 143, 143 ], [65, 105, 225 ], [139, 69, 19 ], [250, 128, 114 ], [244, 164, 96 ], [46, 139, 87 ], [255, 245, 238 ], [160, 82, 45 ], [192, 192, 192 ], [135, 206, 235 ], [106, 90, 205 ], [112, 128, 144 ], [112, 128, 144 ], [255, 250, 250 ], [0, 255, 127 ], [70, 130, 180 ], [210, 180, 140 ], [0, 128, 128 ], [216, 191, 216 ], [255, 99, 71 ], [64, 224, 208 ], [238, 130, 238 ], [245, 222, 179 ], [255, 255, 255 ], [245, 245, 245 ], [255, 255, 0 ], [154, 205, 50 ] ]}
	windowList=None
	lineRegion=None
	windowEdit=None
	COLOR=re.compile(r"#(?P<hex_color>\w+)|(?P<rgb_color>rgb\s*a?\(\s*\d*\s*\,\s*\d*\s*\,\s*\d*\s*\,?\s*\d*\.?\d*\s*\)?)|(?P<hsl_color>hsl\s*a?\(\s*\d*\.?\d*\s*\,\s*\d*\.?\d*\%?\s*\,\s*\d*\.?\d*\%?\s*\,?\s*\d*\.?\d*\s*\)?)|(?P<hsv_color>hsv\s*a?\(\s*\d*\.?\d*\s*\,\s*\d*\.?\d*\%?\s*\,\s*\d*\.?\d*\%?\s*\,?\d*\.?\d*\s*\)?)|(?<!#)(?P<name_color>[a-z]+)")
	RGB=re.compile(r"(?P<rgba_color>rgb\s*a?)\(\s*(?P<r_color>\d*)\s*\,\s*(?P<g_color>\d*)\s*\,\s*(?P<b_color>\d*)\s*\,?\s*(?P<a_color>\d*\.?\d*)?\s*\)?")
	HSL=re.compile(r"(?P<hsla_color>hsl\s*a?)\(\s*(?P<h_color>\d*\.?\d*)\s*\,\s*(?P<s_color>\d*\.?\d*)\%?\s*\,\s*(?P<l_color>\d*\.?\d*)\%?\s*\,?\s*(?P<a_color>\d*\.?\d*)?\s*\)?")
	HSV=re.compile(r"(?P<hsva_color>hsv\s*a?)\(\s*(?P<h_color>\d*\.?\d*)\s*\,\s*(?P<s_color>\d*\.?\d*)\%?\s*\,\s*(?P<v_color>\d*\.?\d*)\%?\s*\,?\s*(?P<a_color>\d*\.?\d*)?\s*\)?")
	def run(self, edit):
		sel=self.view.sel()
		if len(sel) > 0:
			self.windowEdit=edit
			self.lineSelect=sel[0]
			s=self.view.substr(self.view.full_line(sel[0]))
			a=self.view.rowcol(sel[0].begin())
			match,matchRegion,k,v=self._getMatch(s,a)
			match=self._convert(k,v)
			# matchList=None
			# viewList=None
			# typeList=["name","hex","rgb","hsl","hsv"]
			# if match:
			# 	matchList=self._search(match)
			# if matchList:
			# 	viewList=["name : "+matchList["name"],"hex : "+"#"+matchList["hex"],"rgb : "+matchList["rgb"][3],"hsl : "+matchList["hsl"][3],"hsv : "+matchList["hsv"][3]]
			if match:
				self.windowList=match
				self.lineRegion=matchRegion
				self.view.show_popup_menu(match,self.onDone)
	def _getMatch(self, s,a):
		f=re.finditer(self.COLOR,s)
		if f:
			i=0
			for m in f:
				if m.start() <= a[1] and m.end() >= a[1]:
					x=self.view.text_point(a[0],m.start())
					key=None
					value=None
					for k,v in m.groupdict().items():
						if v:
							key=k
							value=v
					return (None,sublime.Region(x,x+(m.end()-m.start())),key,value)
					# return (m.group(),sublime.Region(x,x+(m.end()-m.start())),key,value)
				i+=1
			return None
	def onDone(self, p):
		if p > -1:
			result=re.match(r"\w+\s\:\s(.+)",self.windowList[p]).group(1)
			if self.windowList[p] != "name : - none -":
				self.view.replace(self.windowEdit,self.lineRegion,result)
			self.windowList=None
			self.lineRegion=None
			self.windowEdit=None
	def _search(self, s):
		c=re.compile(r"#|rgb|rgba|hsl|hsv|[a-z]+")
		r=c.search(s)
		if r:
			return self._isValid(r.group(), s)
		else:
			return None
	def _convert(self,k,v):
		a=None
		if k=="hex_color":
			if len(v) > 6:
				a=self._rod2(int("0x"+v[-2:],16)/255)
				tohex="#"+v[:-2]
				tohexa="#"+v
			else:
				a=1.0
				tohex="#"+v
				tohexa="#"+v+"FF"
			toname,tohexfromname=self._getName("hex",tohex[1:])
			if toname == None:
				toname="- none -"
			bgr=self.HexToRgb(tohex[1:])
			torgb=bgr[3]
			torgba="rgba"+torgb[3:-1]+", "+str(a)+")"
			tohsl=self.RgbToHsl(bgr[0],bgr[1],bgr[2])[3]
			tohsla="hsla"+tohsl[3:-1]+", "+str(a)+")"
			tohsv=self.RgbToHsv(bgr[0],bgr[1],bgr[2])[3]
			tohsva="hsva"+tohsv[3:-1]+", "+str(a)+")"
			print("hex",toname,torgb,torgba,tohsl,tohsla,tohsv,tohsva,tohex,tohexa,v)
			return ["name : "+toname,"hex : "+tohex,"hexA : "+tohexa,"rgb : "+torgb,"rgba : "+torgba,"hsl : "+tohsl,"hsla : "+tohsla,"hsv : "+tohsv,"hsva : "+tohsva]
		elif k=="rgb_color":
			m=self.RGB.match(v)
			rgba=m.group("rgba_color")
			r=float(m.group("r_color"))
			g=float(m.group("g_color"))
			b=float(m.group("b_color"))
			if len(m.groupdict()["a_color"]) > 0:
				a=float(m.groupdict()["a_color"])
			else:
				a=1.0
			tohex="#"+self.RgbToHex(r,g,b)
			tohexa=tohex+str("%02X" % int(a*255))
			toname,tohexfromname=self._getName("hex",tohex[1:])
			if toname == None:
				toname="- none -"
			torgb="rgb("+str(self._rod(r))+", "+str(self._rod(g))+", "+str(self._rod(b))+")"
			torgba="rgba"+torgb[3:-1]+", "+str(a)+")"
			tohsl=self.RgbToHsl(r,g,b)[3]
			tohsla="hsla"+tohsl[3:-1]+", "+str(a)+")"
			tohsv=self.RgbToHsv(r,g,b)[3]
			tohsva="hsva"+tohsv[3:-1]+", "+str(a)+")"
			print("rgb",toname,torgb,torgba,tohsl,tohsla,tohsv,tohsva,tohex,tohexa,v)
			return ["name : "+toname,"hex : "+tohex,"hexA : "+tohexa,"rgb : "+torgb,"rgba : "+torgba,"hsl : "+tohsl,"hsla : "+tohsla,"hsv : "+tohsv,"hsva : "+tohsva]
		elif k=="hsl_color":
			m=self.HSL.match(v)
			hsla=m.group("hsla_color")
			h=float(m.group("h_color"))
			s=float(m.group("s_color"))
			l=float(m.group("l_color"))
			if len(m.groupdict()["a_color"]) > 0:
				a=float(m.groupdict()["a_color"])
			else:
				a=1.0
			bgr=self.HslToRgb(h,s,l)
			torgb=bgr[3]
			torgba="rgba"+torgb[3:-1]+", "+str(a)+")"
			tohex="#"+self.RgbToHex(bgr[0],bgr[1],bgr[2])
			tohexa=tohex+str("%02X" % int(a*255))
			toname,tohexfromname=self._getName("hex",tohex[1:])
			if toname == None:
				toname="- none -"
			tohsl="hsl("+str(self._rod2(h))+", "+str(self._rod2(s))+"%, "+str(self._rod2(l))+"%)"
			tohsla="hsla"+tohsl[3:-1]+", "+str(a)+")"
			tohsv=self.RgbToHsv(bgr[0],bgr[1],bgr[2])[3]
			tohsva="hsva"+tohsv[3:-1]+", "+str(a)+")"
			print("hsl",toname,torgb,torgba,tohsl,tohsla,tohsv,tohsva,tohex,tohexa,v)
			return ["name : "+toname,"hex : "+tohex,"hexA : "+tohexa,"rgb : "+torgb,"rgba : "+torgba,"hsl : "+tohsl,"hsla : "+tohsla,"hsv : "+tohsv,"hsva : "+tohsva]
		elif k=="hsv_color":
			m=self.HSV.match(v)
			hsva=m.group("hsva_color")
			h=float(m.group("h_color"))
			s=float(m.group("s_color"))
			vv=float(m.group("v_color"))
			if len(m.groupdict()["a_color"]) > 0:
				a=float(m.groupdict()["a_color"])
			else:
				a=1.0
			bgr=self.HsvToRgb(h,s,vv)
			torgb=bgr[3]
			torgba="rgba"+torgb[3:-1]+", "+str(a)+")"
			tohex="#"+self.RgbToHex(bgr[0],bgr[1],bgr[2])
			tohexa=tohex+str("%02X" % int(a*255))
			toname,tohexfromname=self._getName("hex",tohex[1:])
			if toname == None:
				toname="- none -"
			tohsl=self.RgbToHsl(bgr[0],bgr[1],bgr[2])[3]
			tohsla="hsla"+tohsl[3:-1]+", "+str(a)+")"
			tohsv="hsv("+str(self._rod2(h))+", "+str(self._rod2(s))+", "+str(self._rod2(vv))+")"
			tohsva="hsva"+tohsv[3:-1]+", "+str(a)+")"
			print("hsv",toname,torgb,torgba,tohsl,tohsla,tohsv,tohsva,tohex,tohexa,v)
			return ["name : "+toname,"hex : "+tohex,"hexA : "+tohexa,"rgb : "+torgb,"rgba : "+torgba,"hsl : "+tohsl,"hsla : "+tohsla,"hsv : "+tohsv,"hsva : "+tohsva]
		elif k=="name_color":
			toname,tohexfromname=self._getName("name",v)
			if toname:
				a=1.0
				tohex="#"+tohexfromname
				tohexa=tohex+"FF"
				bgr=self.HexToRgb(tohex[1:])
				torgb=bgr[3]
				torgba="rgba"+torgb[3:-1]+", "+str(a)+")"
				tohsl=self.RgbToHsl(bgr[0],bgr[1],bgr[2])[3]
				tohsla="hsla"+tohsl[3:-1]+", "+str(a)+")"
				tohsv=self.RgbToHsv(bgr[0],bgr[1],bgr[2])[3]
				tohsva="hsva"+tohsv[3:-1]+", "+str(a)+")"
				print("hex",toname,torgb,torgba,tohsl,tohsla,tohsv,tohsva,tohex,tohexa,v)
				return ["name : "+toname,"hex : "+tohex,"hexA : "+tohexa,"rgb : "+torgb,"rgba : "+torgba,"hsl : "+tohsl,"hsla : "+tohsla,"hsv : "+tohsv,"hsva : "+tohsva]
			else:
				return None
	def _getName(self, k,v):
		it=0
		for i in self.colors[k][:]:
			if v.lower() == i:
				return (self.colors["name"][it],self.colors["hex"][it])
			it+=1
		return (None,None)
	def _isValid(self, s, m):
		if s=="#":
			p=re.compile(r".*#(?P<hex_color>.*)")
			r=p.match(m)
			if r:
				if "rgb_color" in r.groups():
					print ("yes")
				else:
					print("no")
				f=self._lookUp("hex",r.group(1).lower())
				if f:
					return f
				else:
					rgb=self.HexToRgb(r.group(1))
					hsv=self.RgbToHsv(rgb[0],rgb[1],rgb[2])
					hsl=self.RgbToHsl(rgb[0],rgb[1],rgb[2])
					hx=r.group(1).upper()
					return {"type":"hex","name":"- none -","hex":hx,"rgb":rgb,"hsl":hsl,"hsv":hsv}
			else:
				return None
		elif s=="rgb" or s=="rgba":
			# p=re.compile(r".*rgb\s?a?\(\s?(?P<r_color>\d*)\s?\,\s?(?P<g_color>\d*)\s?\,\s?(?P<b_color>\d*)\s?\,?\s?(?P<a_color>\d*\.?\d?)?\)?")
			r=self.RGB.match(m)
			if r:
				f=self._lookUp(s,[int(r.group(1)),int(r.group(2)),int(r.group(3))])
				if f:
					return f
				else:
					rgb=[int(r.group(1)),int(r.group(2)),int(r.group(3))]
					hsv=self.RgbToHsv(rgb[0],rgb[1],rgb[2])
					hsl=self.RgbToHsl(rgb[0],rgb[1],rgb[2])
					hx=self.RgbToHex(rgb[0],rgb[1],rgb[2])
					rgb=self.HexToRgb(hx)
					return {"type":"rgb","name":"- none -","hex":hx,"rgb":rgb,"hsl":hsl,"hsv":hsv}
			else:
				return None
		elif s=="hsl" or s=="hsla":
			# p=re.compile(r".*hsl\s?\(\s?(\d*\.?\d*)\s?\,\s?(\d*\.?\d*)\%?\s?\,\s?(\d*\.?\d*)\%?\s?\)?")
			r=self.HSL.match(m)
			if r:
				rgb=self.HslToRgb(float(r.group(1)),float(r.group(2)),float(r.group(3)))
				hsv=self.RgbToHsv(rgb[0],rgb[1],rgb[2])
				hx=self.RgbToHex(rgb[0],rgb[1],rgb[2])
				hsl=self.RgbToHsl(rgb[0],rgb[1],rgb[2])
				name="- none -"
				it=0
				for i in self.colors["hex"]:
					if hx.lower() == i:
						name=self.colors["name"][it]
						break
					it+=1
				return {"type":"hsl","name":name,"hex":hx,"rgb":rgb,"hsl":hsl,"hsv":hsv}
			else:
				return None
		elif s=="hsv" or s=="hsva":
			# p=re.compile(r".*hsv\s?\(\s?(\d*\.?\d*)\s?\,\s?(\d*\.?\d*)\%?\s?\,\s?(\d*\.?\d*)\%?\s?\)?")
			r=self.HSV.match(m)
			if r:
				rgb=self.HsvToRgb(float(r.group(1)),float(r.group(2)),float(r.group(3)))
				hsl=self.RgbToHsl(rgb[0],rgb[1],rgb[2])
				hx=self.RgbToHex(rgb[0],rgb[1],rgb[2])
				hsv=self.RgbToHsv(rgb[0],rgb[1],rgb[2])
				name="- none -"
				it=0
				for i in self.colors["hex"]:
					if hx.lower() == i:
						name=self.colors["name"][it]
						break
					it+=1
				return {"type":"hsl","name":name,"hex":hx,"rgb":rgb,"hsl":hsl,"hsv":hsv}
			else:
				return None
		else:
			r=self._lookUp("name",m)
			if r:
				return r
			else:
				return None
	def _lookUp(self, s, m):
		r=self.colors[s]
		if r:
			it=0
			for i in r[:]:
				if m == i:
					hsl=self.RgbToHsl(self.colors['rgb'][it][0],self.colors['rgb'][it][1],self.colors['rgb'][it][2])
					hsv=self.RgbToHsv(self.colors['rgb'][it][0],self.colors['rgb'][it][1],self.colors['rgb'][it][2])
					strx="rgb("+str(self.colors['rgb'][it][0])+", "+str(self.colors['rgb'][it][1])+", "+str(self.colors['rgb'][it][2])+")"
					return {"type":"name","name":self.colors["name"][it],"hex":self.colors["hex"][it].upper(),"rgb":[self.colors['rgb'][it][0],self.colors['rgb'][it][1],self.colors['rgb'][it][2],strx],"hsl":hsl,"hsv":hsv}
				it+=1
			return None
		else:
			return None
	def RgbToHex(self,r,g,b):
		return "%02X%02X%02X" % (r, g, b)
	def RgbToHsl(self, r, g, b):
		r/=255
		g/=255
		b/=255
		mx=max(r,g,b)
		mn=min(r,g,b)
		l=(mx+mn)/2
		if mx == mn:
			h=s=0
		else:
			d=mx-mn
			if l>0.5:
				s=d/(2-mx-mn)
			else:
				s=d/(mx+mn)
			if mx == r:
				c=0
				if g<b:
					c=6
				h = (g - b) / d + c
			elif mx == g:
				h = (b - r) / d + 2
			elif mx == b:
				h = (r - g) / d + 4
			h/=6
		strx="hsl("+str(self._rod2(h*360))+", "+str(self._rod2(s*100))+"%, "+str(self._rod2(l*100))+"%)"
		return [self._rod2(h*360),self._rod2(s*100),self._rod2(l*100),strx]
	def RgbToHsv(self, r, g, b):
		r/=255
		g/=255
		b/=255
		mx=max(r,g,b)
		mn=min(r,g,b)
		v=mx
		d=mx-mn
		s=d/mx
		if mx==0:
			s=0
		if mx==mn:
			h=0
		else:
			if r==mx:
				h=(g - b) / d
				if g < b:
					h=(g - b) / d +6
			if g==mx:
				h = (b - r) / d + 2
			if b==mx:
				h = (r - g) / d + 4
			h/=6
		strx="hsv("+str(self._rod2(h*360))+", "+str(self._rod2(s*100))+"%, "+str(self._rod2(v*100))+"%)"
		return [self._rod2(h*360),self._rod2(s*100),self._rod2(v*100),strx]
	def HexToRgb(self, hx):
		r=int("0x"+hx[0:2],16)
		g=int("0x"+hx[2:4],16)
		b=int("0x"+hx[4:6],16)
		strx="rgb("+str(r)+", "+str(g)+", "+str(b)+")"
		return [r,g,b,strx]
	def HslToRgb(self, h, s, l):
		h/=360
		s/=100
		l/=100
		if s == 0:
			r=g=b=l
		else:
			if l < 0.5:
				q=l* (1 + s)
			else:
				q=l + s - l * s
			p = 2 * l - q
			r = self._hue2rgb(p, q, h + 1 / 3)
			g = self._hue2rgb(p, q, h)
			b = self._hue2rgb(p, q, h - 1 / 3)
		strx="rgb("+str(self._rod(r*255))+", "+str(self._rod(g*255))+", "+str(self._rod(b*255))+")"
		return [self._rod(r*255),self._rod(g*255),self._rod(b*255),strx]
	def HsvToRgb(self, h, s, v):
		h/=360
		s/=100
		v/=100
		r=g=b=0
		i = math.floor(h * 6)
		f = h * 6 - i
		p = v * (1 - s)
		q = v * (1 - f * s)
		t = v * (1 - (1 - f) * s)
		if (i % 6) ==0:
			r = v
			g = t
			b = p
		if (i % 6) ==1:
			r = q
			g = v
			b = p
		if (i % 6) ==2:
			r = p
			g = v
			b = t
		if (i % 6) ==3:
			r = p
			g = q
			b = v
		if (i % 6) ==4:
			r = t
			g = p
			b = v
		if (i % 6) ==5:
			r = v
			g = p
			b = q
		strx="rgb("+str(self._rod(r*255))+", "+str(self._rod(g*255))+", "+str(self._rod(b*255))+")"
		return [self._rod(r*255),self._rod(g*255),self._rod(b*255),strx]
	def _hue2rgb(self,p,q,t):
		if t < 0:
			t += 1
		if t > 1:
			t -= 1
		if t < 1 / 6:
			return p + (q - p) * 6 * t
		if t < 1 / 2:
			return q
		if t < 2 / 3:
			return p + (q - p) * (2 / 3 - t) * 6
		return p
	def _rod(self, no):
		return int(no//1 + ((no%1)/0.5)//1)
	def _rod2(self, no):
		return round(no,2)

