import { Box, Button, Container, Grid, Typography } from "@mui/material";
import React from "react";

export const HomePageContent = () => {
  return (
    <Grid
      container
      direction="column"
      //   alignItems="center"
      justifyContent="center"
      sx={{ minHeight: "100vh" }}
    >
      <Typography variant="h2">Rent a Slingshot in Atlanta!</Typography>
      <Typography paragraph>
        Colex in Atlanta, GA offers Polaris Slingshot rentals for an
        unforgettable experience. Take the wheel of a Slingshot and drive around
        town, or take a joyride to the countryside for the ultimate adventure!
      </Typography>
      <Box>
        <Button>Book now!</Button>
        <Button>Contact</Button>
      </Box>
    </Grid>
  );
};
