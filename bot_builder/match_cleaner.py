from bot_builder.screen_matcher import screen_matcher

class match_cleaner:
	raw_positions = ([(0,0)], [(0,0)])
	raw_centers = []
	cleaned_positions = ([], [])
	cleaned_centers = []

	def __init__(self, positions):
		self.cleaned_positions=([], []);
		self.cleaned_centers = [];
		self.raw_positions = positions;
		self.raw_centers = [];
		for i in range(len(self.raw_positions[0])):
			center_x = (self.raw_positions[0][i][0] + self.raw_positions[1][i][0])/2
			center_y = (self.raw_positions[0][i][1] + self.raw_positions[1][i][1])/2
			self.raw_centers.append((center_x, center_y));

		self.cleanRaw();

	def set_raw_pos(self, positions):
		self.cleaned_positions=([], []);
		self.cleaned_centers = [];
		self.raw_positions = positions;
		self.raw_centers = [];
		for i in range(len(self.raw_positions[0])):
			center_x = (self.raw_positions[0][i][0] + self.raw_positions[1][i][0])/2
			center_y = (self.raw_positions[0][i][1] + self.raw_positions[1][i][1])/2
			self.raw_centers.append((center_x, center_y));
			#print self.raw_centers[i];
		self.cleanRaw();

	def clean_raw(self):
		if self.raw_positions[0] == []:
			self.cleaned_positions = self.raw_positions;
			self.cleaned_centers = [];
			return;
		self.cleaned_positions[0].append(self.raw_positions[0][0]);
		self.cleaned_positions[1].append(self.raw_positions[1][0]);

		self.cleaned_centers.append(self.raw_centers[0]);
		for i in range(1, len(self.raw_centers)):
			raw_x = self.raw_centers[i][0];
			raw_y = self.raw_centers[i][1];
			unique = True;
			for j in range(len(self.cleaned_positions[0])):
				min_x, max_x = self.cleaned_positions[0][j][0], self.cleaned_positions[1][j][0];
				min_y, max_y = self.cleaned_positions[0][j][1], self.cleaned_positions[1][j][1];
				if (raw_x>=min_x and raw_x<=max_x and raw_y>=min_y and raw_y<=max_y):
					unique = False;
			if unique:
				#print("I'm special");
				self.cleaned_centers.append(self.raw_centers[i]);
				self.cleaned_positions[0].append(self.raw_positions[0][i]);
				self.cleaned_positions[1].append(self.raw_positions[1][i]);

	def get_positions(self):
		return self.cleaned_positions;

	def get_centers(self):
		return self.cleaned_centers;


	def print_self(self):
		print("raw_center(s): " + str(self.raw_centers));
		print("\nclean_center(s): " + str(self.cleaned_centers));
