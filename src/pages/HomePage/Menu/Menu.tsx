import * as React from "react";
import Button from "@mui/material/Button";
import Menu from "@mui/material/Menu";
import MenuItem from "@mui/material/MenuItem";
interface MenuPopoverProps {
  open: boolean;

  onClose: () => void;
  anchorEl: Element | ((element: Element) => Element);
}
export const MenuPopover: React.FC<MenuPopoverProps> = ({
  open,

  onClose,
  anchorEl,
}) => {
  return (
    <div>
      <Button
        id="basic-button"
        aria-controls={open ? "basic-menu" : undefined}
        aria-haspopup="true"
        aria-expanded={open ? "true" : undefined}
      >
        Dashboard
      </Button>
      <Menu
        id="basic-menu"
        anchorEl={anchorEl}
        open={open}
        onClose={onClose}
        MenuListProps={{
          "aria-labelledby": "basic-button",
        }}
      >
        <MenuItem onClick={onClose}>Book a ride</MenuItem>
        <MenuItem onClick={onClose}>Contact Us</MenuItem>
        <MenuItem onClick={onClose}>About us</MenuItem>
      </Menu>
    </div>
  );
};
